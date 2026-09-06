# Show Answer Button Pressed

## language

Language used for the ease button labels shown after answering a card.

Supported values: `en` (English), `ga` (Irish / Gaeilge), or `custom` to use `custom_labels` (see below). Any other value not recognized here also falls back to `custom_labels`, using the English label for any ease left blank there.

Default: `en`

## custom_labels

Custom text for the Again/Hard/Good/Easy labels, used when `language` is set to a value other than `en` or `ga`. Keys are the ease as a string (`"1"` again, `"2"` hard, `"3"` good, `"4"` easy). Leave a value blank to fall back to the English label for that ease.

Default: all blank (falls back to English).

## debug_always_show

When `true`, keeps the label visible at all times (shows `?` on the question side and the ease label on the answer side) instead of auto-hiding after `hide_duration_ms`. Useful for tweaking position/styling. Default: `false`.

## hide_duration_ms

How long (in milliseconds) the label stays visible after answering a card before auto-hiding. Default: `1500`.
