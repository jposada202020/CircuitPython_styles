# SPDX-FileCopyrightText: Jose David Montoya
#
# SPDX-License-Identifier: MIT

"""
`styles`
========
"""

try:
    from typing import Any, Tuple, List
except ImportError:
    pass


def apply_style(target, style):
    """
    :param target: widget object
    :param style: Style to apply


    apply_style could be used in certain libraries that provide access to the color setter.


    **Quickstart: Importing and using apply_style**

    Here is one war of importing ``apply_style`` function so you can use it as
    the name ``colors`` and the color set ``DarkAmber``:

    .. code-block:: python

        from Adafruit_CircuitPython_Styles import apply_style
        from Adafruit_CircuitPython_Styles.styles import DarkAmber

    For a created Label object in ``adafruit_display_text``

    .. code-block:: python

        text_area = bitmap_label.Label(terminalio.FONT, text="Hello", x=10, y=10)

    you can apply the style library using:

     .. code-block:: python

        apply_style(text_area, DarkAmber)

    The function will verify the object and apply the changes according to the features available

    """
    text_display = ["Label", "Bitmap_label"]
    annotation_widget = ["Annotation"]
    progress_bar = ["HorizontalProgressBar"]
    buttons = ["Button"]

    identifier = target.__class__.__name__

    if identifier in text_display:
        target.color = style["TEXT"]
        target.background_color = style["BACKGROUND"]
    elif identifier in annotation_widget:
        target.text_color = style["TEXT"]
    elif identifier in progress_bar:
        target.bar_color = style["BACKGROUND"]
        target.border_color = style["LINE_COLOR"]
    elif identifier in buttons:
        target.fill_color = style["BACKGROUND"]
        target.label_color = style["TEXT"]
        target.outline_color = style["BORDER"]
    else:
        raise Exception("Not yet implemented")


def color_to_tuple(value):
    """Converts a color from a 24-bit integer to a tuple.
    :param value: RGB LED desired value - can be a RGB tuple or a 24-bit integer.
    """
    if isinstance(value, tuple):
        return value
    if isinstance(value, int):
        if value >> 24:
            raise ValueError("Only bits 0->23 valid for integer input")
        r = value >> 16
        g = (value >> 8) & 0xFF
        b = value & 0xFF
        return [r, g, b]

    raise ValueError("Color must be a tuple or 24-bit integer value.")


def color_fade(start_color: int, end_color: int, fraction: float):
    """Linear extrapolation of a color between two RGB colors (tuple or 24-bit integer).
    :param start_color: starting color
    :param end_color: ending color
    :param fraction: Floating point number  ranging from 0 to 1 indicating what
    fraction of interpolation between start_color and end_color.
    """

    start_color = color_to_tuple(start_color)
    end_color = color_to_tuple(end_color)
    if fraction >= 1:
        return end_color
    if fraction <= 0:
        return start_color

    faded_color = [0, 0, 0]
    for i in range(3):
        faded_color[i] = start_color[i] - int(
            (start_color[i] - end_color[i]) * fraction
        )
    return faded_color
