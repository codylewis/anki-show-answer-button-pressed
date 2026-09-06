from aqt import gui_hooks, mw
from aqt.reviewer import Reviewer
from aqt.qt import QLabel, QObject, QEvent, Qt, QTimer

LANGUAGES = {
    "en": {1: "Again", 2: "Hard", 3: "Good", 4: "Easy"},
    "ga": {1: "Arís", 2: "Deacair", 3: "Go Maith", 4: "Éasca"},
}

BUTTON_COLORS = {
    1: "rgba(170,51,51,0.33)",
    2: "rgba(204,119,0,0.33)",
    3: "rgba(0,170,0,0.33)",
    4: "rgba(0,108,255,0.33)",
}


def _button_style(ease: int):
    config = mw.addonManager.getConfig(__name__) or {}
    language = config.get("language", "en")
    labels = LANGUAGES.get(language, LANGUAGES["en"])
    return labels.get(ease, str(ease)), BUTTON_COLORS.get(ease, "#000")


SHARED_STYLING = (
    "font-size: 15px; padding: 5px 12px; color: white; "
    "border-top-left-radius: 0; border-top-right-radius: 0; "
    "border-bottom-left-radius: 12px; border-bottom-right-radius: 12px; "
)

LABEL_WIDTH = 85
LABEL_HEIGHT = 30
LABEL_MARGIN_TOP = 0
LABEL_MARGIN_RIGHT = 20


def _debug_always_show() -> bool:
    config = mw.addonManager.getConfig(__name__) or {}
    return bool(config.get("debug_always_show", False))


class _ResizeFilter(QObject):
    def eventFilter(self, _obj, event):
        if event.type() == QEvent.Type.Resize and _state.label:
            _set_label_position()
        return False


class _State:
    label: QLabel | None = None
    hide_timer: QTimer | None = None
    resize_filter: _ResizeFilter | None = None


_state = _State()


def _set_label_position():
    _state.label.setGeometry(
        mw.width() - (LABEL_WIDTH + LABEL_MARGIN_RIGHT),
        LABEL_MARGIN_TOP,
        LABEL_WIDTH,
        LABEL_HEIGHT,
    )


def _ensure_label():
    if _state.label is not None:
        return
    _state.label = QLabel("", mw)
    _state.label.setStyleSheet(SHARED_STYLING)
    _state.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    _state.label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
    _set_label_position()
    _state.label.hide()
    _state.label.raise_()

    _state.hide_timer = QTimer(mw)
    _state.hide_timer.setSingleShot(True)
    _state.hide_timer.timeout.connect(_state.label.hide)

    _state.resize_filter = _ResizeFilter()
    mw.installEventFilter(_state.resize_filter)


old_answerCard = Reviewer._answerCard


def new_answerCard(self, ease: int):
    if self.state != "answer":
        old_answerCard(self, ease)
        return
    _ensure_label()
    old_answerCard(self, ease)

    name, bg_color = _button_style(ease)
    _state.label.setText(name)
    _state.label.setStyleSheet(f"background-color: {bg_color}; {SHARED_STYLING}")
    _state.label.show()
    _state.label.raise_()
    if not _debug_always_show():
        _state.hide_timer.start(1500)


Reviewer._answerCard = new_answerCard


def on_show_question(_card):
    if not _debug_always_show():
        return
    _ensure_label()
    _state.label.setText("?")
    _state.label.setStyleSheet(f"background-color: #000; {SHARED_STYLING}")
    _state.label.show()
    _state.label.raise_()


gui_hooks.reviewer_did_show_question.append(on_show_question)


def on_reviewer_will_close():
    if _state.hide_timer:
        _state.hide_timer.stop()
    if _state.resize_filter:
        mw.removeEventFilter(_state.resize_filter)
        _state.resize_filter = None
    if _state.label:
        _state.label.hide()
    _state.label = None
    _state.hide_timer = None


gui_hooks.reviewer_will_end.append(on_reviewer_will_close)
