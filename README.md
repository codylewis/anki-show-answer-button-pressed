# Show Answer Button Pressed

An Anki add-on that shows which ease button (Again/Hard/Good/Easy) you just pressed as a color-coded label in the top-right corner of the main window, auto-hiding after 1.5 seconds. Handy for confirming you pressed the button you meant to, especially when answering with keyboard shortcuts.

## Screenshots

![Again](screenshots/screenshot-again.png)

![Hard](screenshots/screenshot-hard.png)

![Good](screenshots/screenshot-good.png)

![Easy](screenshots/screenshot-easy.png)

## Configuration

Configurable from **Tools → Add-ons → Show Answer Button Pressed → Config**:

| Key | Description | Default |
| --- | --- | --- |
| `language` | Language for the button labels: `en` (English), `ga` (Irish / Gaeilge), or `custom` to use `custom_labels` instead | `en` |
| `custom_labels` | Custom Again/Hard/Good/Easy text, used when `language` is `custom` (or any other unrecognized value) | blank (falls back to English) |
| `debug_always_show` | Keep the label visible at all times instead of auto-hiding, for tweaking position/styling | `false` |
| `hide_duration_ms` | How long (in milliseconds) the label stays visible after answering before auto-hiding | `1500` |

See [config.md](config.md) for details.

## Installation

Install from AnkiWeb: [ankiweb.net/shared/info/2060144143](https://ankiweb.net/shared/info/2060144143).

## Credits

Inspired by [Color Confirmation](https://ankiweb.net/shared/info/1084228676), itself a modification of an earlier [Answer Confirmation](https://ankiweb.net/shared/info/3882211885) add-on. This is an independent implementation, no code is shared with either.

## License

[MIT](LICENSE)
