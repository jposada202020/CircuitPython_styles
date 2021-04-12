# SPDX-FileCopyrightText: 2021 Jose David M.
#
# SPDX-License-Identifier: MIT

"""
Display Text style definitions. Based on the PySimpleGui styles used under the LGPL3+ license.
"""
# pylint: disable=invalid-name, too-few-public-methods


class GetStyle:
    """
    GetStyle allow any library to use the colorset available.

    **Quickstart: Importing and using GetStyle**

    Here is one war of importing ``GetStyle`` class so you can use it as
    the name ``colors`` and the color set ``BluePurple``:

    .. code-block:: python

        from adafruit_styles.style import GetStyle, BluePurple

    Now you can create a color set using:

    .. code-block:: python

        colors = GetStyle(BluePurple)

    all the four color attributes will be available in colors. This could be easily
    accessed via:

     .. code-block:: python

        colors.text_color

    Currently there are four attributes ``background_color``, ``text_color``, ``line_color`` and
    ``border``

    """

    def __init__(self, color):
        self.background = color["BACKGROUND"]
        self.text_color = color["TEXT"]
        self.border = color["BORDER"]
        self.line_color = color["LINE_COLOR"]


DarkAmber = {
    "BACKGROUND": 0x2C2825,
    "TEXT": 0xFDCB52,
    "BORDER": 0x705E52,
    "LINE_COLOR": 0xFDCB52,
}

DarkBlue = {
    "BACKGROUND": 0x1A2835,
    "TEXT": 0xD1ECFF,
    "BORDER": 0x335267,
    "LINE_COLOR": 0xACC2D0,
}

Reds = {
    "BACKGROUND": 0x280001,
    "TEXT": 0xFFFFFF,
    "BORDER": 0xD8D584,
    "LINE_COLOR": 0x763E00,
}

Green = {
    "BACKGROUND": 0x82A459,
    "TEXT": 0x000000,
    "BORDER": 0xD8D584,
    "LINE_COLOR": 0xE3ECF3,
}

BluePurple = {
    "BACKGROUND": 0xA5CADD,
    "TEXT": 0x6E266E,
    "BORDER": 0xE0F5FF,
    "LINE_COLOR": 0xE0F5FF,
}

Purple = {
    "BACKGROUND": 0xB0AAC2,
    "TEXT": 0x000000,
    "BORDER": 0xF2EFE8,
    "LINE_COLOR": 0xF2EFE8,
}

BlueMono = {
    "BACKGROUND": 0xAAB6D3,
    "TEXT": 0x000000,
    "BORDER": 0xF1F4FC,
    "LINE_COLOR": 0xF1F4FC,
}

GreenMono = {
    "BACKGROUND": 0xA8C1B4,
    "TEXT": 0x000000,
    "BORDER": 0xDDE0DE,
    "LINE_COLOR": 0xE3E3E3,
}

BrownBlue = {
    "BACKGROUND": 0x64778D,
    "TEXT": 0xFFFFFF,
    "BORDER": 0xF0F3F7,
    "LINE_COLOR": 0xA6B2BE,
}

BrightColors = {
    "BACKGROUND": 0xB4FFB4,
    "TEXT": 0x000000,
    "BORDER": 0xFFFF64,
    "LINE_COLOR": 0xFFB482,
}


Material1 = {
    "BACKGROUND": 0xE3F2FD,
    "TEXT": 0x000000,
    "BORDER": 0x86A8FF,
    "LINE_BORDER": 0x5079D3,
}

Material2 = {
    "BACKGROUND": 0xFAFAFA,
    "TEXT": 0x000000,
    "BORDER": 0x5EA7FF,
    "LINE_BORDER": 0x0079D3,
}

Reddit = {
    "BACKGROUND": 0xFFFFFF,
    "TEXT": 0x1A1A1B,
    "BORDER": 0xA5A4A4,
    "LINE_BORDER": 0x0079D3,
}

Topanga = {
    "BACKGROUND": 0x282923,
    "TEXT": 0xE7DB74,
    "BORDER": 0xE7C855,
    "LINE_BORDER": 0x284B5A,
}

GreenTan = {
    "BACKGROUND": 0x9FB8AD,
    "TEXT": 0x000000,
    "BORDER": 0xF7F3EC,
    "LINE_BORDER": 0x475841,
}

Dark = {
    "BACKGROUND": 0x404040,
    "TEXT": 0xFFFFFF,
    "BORDER": 0x707070,
    "LINE_BORDER": 0x004F00,
}

LightGreen = {
    "BACKGROUND": 0xB7CECE,
    "TEXT": 0x000000,
    "BORDER": 0xFDFFF7,
    "LINE_BORDER": 0x658268,
}

Dark2 = {
    "BACKGROUND": 0x404040,
    "TEXT": 0xFFFFFF,
    "BORDER": 0x707070,
    "LINE_BORDER": 0x004F00,
}

Black = {
    "BACKGROUND": 0x000000,
    "TEXT": 0xFFFFFF,
    "BORDER": 0x707070,
    "LINE_BORDER": 0xFFFFFF,
}

Tan = {
    "BACKGROUND": 0xFDF6E3,
    "TEXT": 0x268BD1,
    "BORDER": 0xEEE8D5,
    "LINE_BORDER": 0x063542,
}

TanBlue = {
    "BACKGROUND": 0xE5DECE,
    "TEXT": 0x063289,
    "BORDER": 0xEEE8D5,
    "LINE_BORDER": 0x063289,
}

DarkTanBlue = {
    "BACKGROUND": 0x242834,
    "TEXT": 0xDFE6F8,
    "BORDER": 0xA9AFBB,
    "LINE_BORDER": 0x063289,
}

NeutralBlue = {
    "BACKGROUND": 0x92AA9D,
    "TEXT": 0x000000,
    "BORDER": 0xFCFFF6,
    "LINE_BORDER": 0xD0DBBD,
}
Kayak = {
    "BACKGROUND": 0xA7AD7F,
    "TEXT": 0x000000,
    "BORDER": 0xE6D3A8,
    "LINE_BORDER": 0x5D907D,
}
SandyBeach = {
    "BACKGROUND": 0xEFECCB,
    "TEXT": 0x012F2F,
    "BORDER": 0xE6D3A8,
    "LINE_BORDER": 0x046380,
}
TealMono = {
    "BACKGROUND": 0xA8CFDD,
    "TEXT": 0x000000,
    "BORDER": 0xDFEDF2,
    "LINE_BORDER": 0x183440,
}
LightBlue = {
    "BACKGROUND": 0xE3F2FD,
    "TEXT": 0x000000,
    "BORDER": 0x86A8FF,
    "LINE_BORDER": 0x5079D3,
}
LightGrey = {
    "BACKGROUND": 0xFAFAFA,
    "TEXT": 0x000000,
    "BORDER": 0x5EA7FF,
    "LINE_BORDER": 0x0079D3,
}
LightGrey1 = {
    "BACKGROUND": 0xFFFFFF,
    "TEXT": 0x1A1A1B,
    "BORDER": 0xA5A4A4,
    "LINE_BORDER": 0x0079D3,
}
DarkBrown = {
    "BACKGROUND": 0x282923,
    "TEXT": 0xE7DB74,
    "BORDER": 0xE7C855,
    "LINE_BORDER": 0x284B5A,
}
LightGreen1 = {
    "BACKGROUND": 0x9FB8AD,
    "TEXT": 0x000000,
    "BORDER": 0xF7F3EC,
    "LINE_BORDER": 0x475841,
}
DarkGrey = {
    "BACKGROUND": 0x404040,
    "TEXT": 0xFFFFFF,
    "BORDER": 0x707070,
    "LINE_BORDER": 0x004F00,
}
LightGreen2 = {
    "BACKGROUND": 0xB7CECE,
    "TEXT": 0x000000,
    "BORDER": 0xFDFFF7,
    "LINE_BORDER": 0x658268,
}
DarkGrey1 = {
    "BACKGROUND": 0x404040,
    "TEXT": 0xFFFFFF,
    "BORDER": 0x707070,
    "LINE_BORDER": 0x004F00,
}
DarkBlack = {
    "BACKGROUND": 0x000000,
    "TEXT": 0xFFFFFF,
    "BORDER": 0x707070,
    "LINE_BORDER": 0xFFFFFF,
}
LightBrown = {
    "BACKGROUND": 0xFDF6E3,
    "TEXT": 0x268BD1,
    "BORDER": 0xEEE8D5,
    "LINE_BORDER": 0x063542,
}
LightBrown1 = {
    "BACKGROUND": 0xE5DECE,
    "TEXT": 0x063289,
    "BORDER": 0xEEE8D5,
    "LINE_BORDER": 0x063289,
}
DarkBlue1 = {
    "BACKGROUND": 0x242834,
    "TEXT": 0xDFE6F8,
    "BORDER": 0xA9AFBB,
    "LINE_BORDER": 0x063289,
}
DarkBrown1 = {
    "BACKGROUND": 0x2C2825,
    "TEXT": 0xFDCB52,
    "BORDER": 0x705E52,
    "LINE_BORDER": 0xFDCB52,
}
DarkBlue2 = {
    "BACKGROUND": 0x1A2835,
    "TEXT": 0xD1ECFF,
    "BORDER": 0x1B6497,
    "LINE_BORDER": 0xFAFAF8,
}
DarkBrown2 = {
    "BACKGROUND": 0x280001,
    "TEXT": 0xFFFFFF,
    "BORDER": 0x763E00,
    "LINE_BORDER": 0xDAAD28,
}
DarkGreen = {
    "BACKGROUND": 0x82A459,
    "TEXT": 0x000000,
    "BORDER": 0xE3ECF3,
    "LINE_BORDER": 0x517239,
}
LightBlue1 = {
    "BACKGROUND": 0xA5CADD,
    "TEXT": 0x6E266E,
    "BORDER": 0xE0F5FF,
    "LINE_BORDER": 0x303952,
}
LightPurple = {
    "BACKGROUND": 0xB0AAC2,
    "TEXT": 0x000000,
    "BORDER": 0xF2EFE8,
    "LINE_BORDER": 0xC2D4D8,
}
LightBlue2 = {
    "BACKGROUND": 0xAAB6D3,
    "TEXT": 0x000000,
    "BORDER": 0xF1F4FC,
    "LINE_BORDER": 0x7186C7,
}
LightGreen3 = {
    "BACKGROUND": 0xA8C1B4,
    "TEXT": 0x000000,
    "BORDER": 0xE3E3E3,
    "LINE_BORDER": 0x6D9F85,
}
DarkBlue3 = {
    "BACKGROUND": 0x64778D,
    "TEXT": 0xFFFFFF,
    "BORDER": 0xA6B2BE,
    "LINE_BORDER": 0x283B5B,
}
LightGreen4 = {
    "BACKGROUND": 0xB4FFB4,
    "TEXT": 0x000000,
    "BORDER": 0xFFB482,
    "LINE_BORDER": 0xFFA0DC,
}
LightGreen5 = {
    "BACKGROUND": 0x92AA9D,
    "TEXT": 0x000000,
    "BORDER": 0xFCFFF6,
    "LINE_BORDER": 0xD0DBBD,
}
LightBrown2 = {
    "BACKGROUND": 0xA7AD7F,
    "TEXT": 0x000000,
    "BORDER": 0xE6D3A8,
    "LINE_BORDER": 0x5D907D,
}
LightBrown3 = {
    "BACKGROUND": 0xEFECCB,
    "TEXT": 0x012F2F,
    "BORDER": 0xE6D3A8,
    "LINE_BORDER": 0x046380,
}
LightBlue3 = {
    "BACKGROUND": 0xA8CFDD,
    "TEXT": 0x000000,
    "BORDER": 0xDFEDF2,
    "LINE_BORDER": 0x183440,
}
LightBrown4 = {
    "BACKGROUND": 0xD7C79E,
    "TEXT": 0xA35638,
    "BORDER": 0xA35638,
    "LINE_BORDER": 0xA35638,
}
DarkTeal = {
    "BACKGROUND": 0x003F5C,
    "TEXT": 0xFB5B5A,
    "BORDER": 0xBC4873,
    "LINE_BORDER": 0xFB5B5A,
}
DarkPurple = {
    "BACKGROUND": 0x472B62,
    "TEXT": 0xFB5B5A,
    "BORDER": 0xBC4873,
    "LINE_BORDER": 0x472B62,
}
LightGreen6 = {
    "BACKGROUND": 0xEAFBEA,
    "TEXT": 0x1F6650,
    "BORDER": 0x1F6650,
    "LINE_BORDER": 0x1F6650,
}
DarkGrey2 = {
    "BACKGROUND": 0x2B2B28,
    "TEXT": 0xF8F8F8,
    "BORDER": 0xF1D6AB,
    "LINE_BORDER": 0xE3B04B,
}
LightBrown6 = {
    "BACKGROUND": 0xF9B282,
    "TEXT": 0x8F4426,
    "BORDER": 0x8F4426,
    "LINE_BORDER": 0x8F4426,
}
DarkTeal1 = {
    "BACKGROUND": 0x396362,
    "TEXT": 0xFFE7D1,
    "BORDER": 0xF6C89F,
    "LINE_BORDER": 0x4B8E8D,
}
LightBrown7 = {
    "BACKGROUND": 0xF6C89F,
    "TEXT": 0x396362,
    "BORDER": 0x396362,
    "LINE_BORDER": 0x396362,
}
DarkPurple1 = {
    "BACKGROUND": 0x0C093C,
    "TEXT": 0xFAD6D6,
    "BORDER": 0xEEA5F6,
    "LINE_BORDER": 0xDF42D1,
}
DarkGrey3 = {
    "BACKGROUND": 0x211717,
    "TEXT": 0xDFDDC7,
    "BORDER": 0xF58B54,
    "LINE_BORDER": 0xA34A28,
}
LightBrown8 = {
    "BACKGROUND": 0xDFDDC7,
    "TEXT": 0x211717,
    "BORDER": 0x211717,
    "LINE_BORDER": 0xA34A28,
}
DarkBlue4 = {
    "BACKGROUND": 0x494CA2,
    "TEXT": 0xE3E7F1,
    "BORDER": 0xC6CBEF,
    "LINE_BORDER": 0x8186D5,
}
LightBlue4 = {
    "BACKGROUND": 0x5C94BD,
    "TEXT": 0x470938,
    "BORDER": 0x470938,
    "LINE_BORDER": 0x470938,
}
DarkTeal2 = {
    "BACKGROUND": 0x394A6D,
    "TEXT": 0xC0FFB3,
    "BORDER": 0x52DE97,
    "LINE_BORDER": 0x394A6D,
}
DarkTeal3 = {
    "BACKGROUND": 0x3C9D9B,
    "TEXT": 0xC0FFB3,
    "BORDER": 0x52DE97,
    "LINE_BORDER": 0x394A6D,
}
DarkPurple5 = {
    "BACKGROUND": 0x730068,
    "TEXT": 0xF6F078,
    "BORDER": 0x01D28E,
    "LINE_BORDER": 0x730068,
}
DarkPurple2 = {
    "BACKGROUND": 0x202060,
    "TEXT": 0xB030B0,
    "BORDER": 0x602080,
    "LINE_BORDER": 0x202040,
}
DarkBlue5 = {
    "BACKGROUND": 0x000272,
    "TEXT": 0xFF6363,
    "BORDER": 0xA32F80,
    "LINE_BORDER": 0x341677,
}
LightGrey2 = {
    "BACKGROUND": 0xF6F6F6,
    "TEXT": 0x420000,
    "BORDER": 0x420000,
    "LINE_BORDER": 0xD4D7DD,
}
LightGrey3 = {
    "BACKGROUND": 0xEAE9E9,
    "TEXT": 0x420000,
    "BORDER": 0x420000,
    "LINE_BORDER": 0xD4D7DD,
}
DarkBlue6 = {
    "BACKGROUND": 0x01024E,
    "TEXT": 0xFF6464,
    "BORDER": 0x8B4367,
    "LINE_BORDER": 0x543864,
}
DarkBlue7 = {
    "BACKGROUND": 0x241663,
    "TEXT": 0xEAE7AF,
    "BORDER": 0xA72693,
    "LINE_BORDER": 0x160F30,
}
LightBrown9 = {
    "BACKGROUND": 0xF6D365,
    "TEXT": 0x3A1F5D,
    "BORDER": 0x3A1F5D,
    "LINE_BORDER": 0xC83660,
}
DarkPurple3 = {
    "BACKGROUND": 0x6E2142,
    "TEXT": 0xFFD692,
    "BORDER": 0xE16363,
    "LINE_BORDER": 0x943855,
}
LightBrown10 = {
    "BACKGROUND": 0xFFD692,
    "TEXT": 0x6E2142,
    "BORDER": 0x6E2142,
    "LINE_BORDER": 0x6E2142,
}
DarkPurple4 = {
    "BACKGROUND": 0x200F21,
    "TEXT": 0xF638DC,
    "BORDER": 0x5A3D5C,
    "LINE_BORDER": 0x382039,
}
LightBlue5 = {
    "BACKGROUND": 0xB2FCFF,
    "TEXT": 0x3E64FF,
    "BORDER": 0x3E64FF,
    "LINE_BORDER": 0x3E64FF,
}
DarkTeal4 = {
    "BACKGROUND": 0x464159,
    "TEXT": 0xC7F0DB,
    "BORDER": 0x8BBABB,
    "LINE_BORDER": 0x6C7B95,
}
LightTeal = {
    "BACKGROUND": 0xC7F0DB,
    "TEXT": 0x464159,
    "BORDER": 0x464159,
    "LINE_BORDER": 0x464159,
}
DarkTeal5 = {
    "BACKGROUND": 0x8BBABB,
    "TEXT": 0x464159,
    "BORDER": 0x464159,
    "LINE_BORDER": 0x6C7B95,
}
LightGrey4 = {
    "BACKGROUND": 0xFAF5EF,
    "TEXT": 0x672F2F,
    "BORDER": 0x672F2F,
    "LINE_BORDER": 0x99B19C,
}
LightGreen7 = {
    "BACKGROUND": 0x99B19C,
    "TEXT": 0xFAF5EF,
    "BORDER": 0xD7D1C9,
    "LINE_BORDER": 0x99B19C,
}
LightGrey5 = {
    "BACKGROUND": 0xD7D1C9,
    "TEXT": 0x672F2F,
    "BORDER": 0x672F2F,
    "LINE_BORDER": 0x672F2F,
}
DarkBrown3 = {
    "BACKGROUND": 0xA0855B,
    "TEXT": 0xF9F6F2,
    "BORDER": 0xF1D6AB,
    "LINE_BORDER": 0x38470B,
}
LightBrown11 = {
    "BACKGROUND": 0xF1D6AB,
    "TEXT": 0x38470B,
    "BORDER": 0x38470B,
    "LINE_BORDER": 0xA0855B,
}
DarkRed = {
    "BACKGROUND": 0x83142C,
    "TEXT": 0xF9D276,
    "BORDER": 0xAD1D45,
    "LINE_BORDER": 0xAD1D45,
}
DarkTeal6 = {
    "BACKGROUND": 0x204969,
    "TEXT": 0xFFF7F7,
    "BORDER": 0xDADADA,
    "LINE_BORDER": 0xFFF7F7,
}
DarkBrown4 = {
    "BACKGROUND": 0x252525,
    "TEXT": 0xFF0000,
    "BORDER": 0xAF0404,
    "LINE_BORDER": 0x252525,
}
LightYellow = {
    "BACKGROUND": 0xF4FF61,
    "TEXT": 0x27AA80,
    "BORDER": 0x27AA80,
    "LINE_BORDER": 0x27AA80,
}
DarkGreen1 = {
    "BACKGROUND": 0x2B580C,
    "TEXT": 0xFDEF96,
    "BORDER": 0xF7B71D,
    "LINE_BORDER": 0x2B580C,
}
LightGreen8 = {
    "BACKGROUND": 0xC8DAD3,
    "TEXT": 0x63707E,
    "BORDER": 0x63707E,
    "LINE_BORDER": 0x63707E,
}
DarkTeal7 = {
    "BACKGROUND": 0x248EA9,
    "TEXT": 0xFAFDCB,
    "BORDER": 0xAEE7E8,
    "LINE_BORDER": 0xFAFDCB,
}
DarkBlue8 = {
    "BACKGROUND": 0x454D66,
    "TEXT": 0xD9D872,
    "BORDER": 0x58B368,
    "LINE_BORDER": 0x009975,
}
DarkBlue9 = {
    "BACKGROUND": 0x263859,
    "TEXT": 0xFF6768,
    "BORDER": 0x6B778D,
    "LINE_BORDER": 0x263859,
}
DarkBlue10 = {
    "BACKGROUND": 0x0028FF,
    "TEXT": 0xF1F4DF,
    "BORDER": 0x10EAF0,
    "LINE_BORDER": 0x24009C,
}
DarkBlue11 = {
    "BACKGROUND": 0x6384B3,
    "TEXT": 0xE6F0B6,
    "BORDER": 0xB8E9C0,
    "LINE_BORDER": 0x684949,
}
DarkTeal8 = {
    "BACKGROUND": 0x71A0A5,
    "TEXT": 0x212121,
    "BORDER": 0x212121,
    "LINE_BORDER": 0x665C84,
}
DarkRed1 = {
    "BACKGROUND": 0xC10000,
    "TEXT": 0xEEEEEE,
    "BORDER": 0xDEDEDE,
    "LINE_BORDER": 0xEEEEEE,
}
LightBrown5 = {
    "BACKGROUND": 0xFFF591,
    "TEXT": 0xE41749,
    "BORDER": 0xE41749,
    "LINE_BORDER": 0xE41749,
}
LightGreen9 = {
    "BACKGROUND": 0xF1EDB3,
    "TEXT": 0x3B503D,
    "BORDER": 0x3B503D,
    "LINE_BORDER": 0x3B503D,
}
DarkGreen2 = {
    "BACKGROUND": 0x3B503D,
    "TEXT": 0xF1EDB3,
    "BORDER": 0xC8CF94,
    "LINE_BORDER": 0x3B503D,
}
LightGray1 = {
    "BACKGROUND": 0xF2F2F2,
    "TEXT": 0x222831,
    "BORDER": 0x222831,
    "LINE_BORDER": 0x222831,
}
DarkGrey4 = {
    "BACKGROUND": 0x52524E,
    "TEXT": 0xE9E9E5,
    "BORDER": 0xD4D6C8,
    "LINE_BORDER": 0x9A9B94,
}
DarkBlue12 = {
    "BACKGROUND": 0x324E7B,
    "TEXT": 0xF8F8F8,
    "BORDER": 0x86A6DF,
    "LINE_BORDER": 0x5068A9,
}
DarkPurple6 = {
    "BACKGROUND": 0x070739,
    "TEXT": 0xE1E099,
    "BORDER": 0xC327AB,
    "LINE_BORDER": 0x521477,
}
DarkPurple7 = {
    "BACKGROUND": 0x191930,
    "TEXT": 0xB1B7C5,
    "BORDER": 0xB1B7C5,
    "LINE_BORDER": 0xB1B7C5,
}
DarkBlue13 = {
    "BACKGROUND": 0x203562,
    "TEXT": 0xE3E8F8,
    "BORDER": 0xC0C5CD,
    "LINE_BORDER": 0x3E588F,
}
DarkBrown5 = {
    "BACKGROUND": 0x3C1B1F,
    "TEXT": 0xF6E1B5,
    "BORDER": 0xE2BF81,
    "LINE_BORDER": 0xF6E1B5,
}
DarkGreen3 = {
    "BACKGROUND": 0x062121,
    "TEXT": 0xEEEEEE,
    "BORDER": 0xE4DCAD,
    "LINE_BORDER": 0x181810,
}
DarkBlack1 = {
    "BACKGROUND": 0x181810,
    "TEXT": 0xEEEEEE,
    "BORDER": 0xE4DCAD,
    "LINE_BORDER": 0x062121,
}
DarkGrey5 = {
    "BACKGROUND": 0x343434,
    "TEXT": 0xF3F3F3,
    "BORDER": 0xE9DCBE,
    "LINE_BORDER": 0x8E8B82,
}
LightBrown12 = {
    "BACKGROUND": 0x8E8B82,
    "TEXT": 0xF3F3F3,
    "BORDER": 0xE9DCBE,
    "LINE_BORDER": 0x8E8B82,
}
DarkTeal9 = {
    "BACKGROUND": 0x13445A,
    "TEXT": 0xFEF4E8,
    "BORDER": 0x446878,
    "LINE_BORDER": 0x446878,
}
DarkBlue14 = {
    "BACKGROUND": 0x21273D,
    "TEXT": 0xF1F6F8,
    "BORDER": 0xB9D4F1,
    "LINE_BORDER": 0x6A759B,
}
LightBlue6 = {
    "BACKGROUND": 0xF1F6F8,
    "TEXT": 0x21273D,
    "BORDER": 0x21273D,
    "LINE_BORDER": 0x6A759B,
}
DarkGreen4 = {
    "BACKGROUND": 0x044343,
    "TEXT": 0xE4E4E4,
    "BORDER": 0x045757,
    "LINE_BORDER": 0x045757,
}
DarkGreen5 = {
    "BACKGROUND": 0x1B4B36,
    "TEXT": 0xE0E7F1,
    "BORDER": 0xAEBD77,
    "LINE_BORDER": 0x538F6A,
}
DarkTeal10 = {
    "BACKGROUND": 0x0D3446,
    "TEXT": 0xD8DFE2,
    "BORDER": 0x71ADB5,
    "LINE_BORDER": 0x176D81,
}
DarkGrey6 = {
    "BACKGROUND": 0x3E3E3E,
    "TEXT": 0xEDEDED,
    "BORDER": 0x68868C,
    "LINE_BORDER": 0x405559,
}
DarkTeal11 = {
    "BACKGROUND": 0x405559,
    "TEXT": 0xEDEDED,
    "BORDER": 0x68868C,
    "LINE_BORDER": 0x68868C,
}
LightBlue7 = {
    "BACKGROUND": 0x9ED0E0,
    "TEXT": 0x19483F,
    "BORDER": 0x19483F,
    "LINE_BORDER": 0x19483F,
}
LightGreen10 = {
    "BACKGROUND": 0xD8EBB5,
    "TEXT": 0x205D67,
    "BORDER": 0x205D67,
    "LINE_BORDER": 0x205D67,
}
DarkBlue15 = {
    "BACKGROUND": 0x151680,
    "TEXT": 0xF1FEA4,
    "BORDER": 0x375FC0,
    "LINE_BORDER": 0x1C44AC,
}
DarkBlue16 = {
    "BACKGROUND": 0x1C44AC,
    "TEXT": 0xF1FEA4,
    "BORDER": 0x375FC0,
    "LINE_BORDER": 0x151680,
}
DarkTeal12 = {
    "BACKGROUND": 0x004A7C,
    "TEXT": 0xFAFAFA,
    "BORDER": 0xE8F1F5,
    "LINE_BORDER": 0x005691,
}
LightBrown13 = {
    "BACKGROUND": 0xEBF5EE,
    "TEXT": 0x921224,
    "BORDER": 0x921224,
    "LINE_BORDER": 0x921224,
}
DarkBlue17 = {
    "BACKGROUND": 0x21294C,
    "TEXT": 0xF9F2D7,
    "BORDER": 0xF2DEA8,
    "LINE_BORDER": 0x141829,
}
DarkBrown6 = {
    "BACKGROUND": 0x785E4D,
    "TEXT": 0xF2EEE3,
    "BORDER": 0xBAAF92,
    "LINE_BORDER": 0x785E4D,
}
DarkGreen6 = {
    "BACKGROUND": 0x5C715E,
    "TEXT": 0xF2F9F1,
    "BORDER": 0xDDEEDF,
    "LINE_BORDER": 0x5C715E,
}
DarkGreen7 = {
    "BACKGROUND": 0x0C231E,
    "TEXT": 0xEFBE1C,
    "BORDER": 0x153C33,
    "LINE_BORDER": 0x153C33,
}
DarkGrey7 = {
    "BACKGROUND": 0x4B586E,
    "TEXT": 0xDDDDDD,
    "BORDER": 0x574E6D,
    "LINE_BORDER": 0x43405D,
}
DarkRed2 = {
    "BACKGROUND": 0xAB1212,
    "TEXT": 0xF6E4B5,
    "BORDER": 0xCD3131,
    "LINE_BORDER": 0xAB1212,
}
LightGrey6 = {
    "BACKGROUND": 0xE3E3E3,
    "TEXT": 0x233142,
    "BORDER": 0x233142,
    "LINE_BORDER": 0x455D7A,
}
DarkGrey8 = {
    "BACKGROUND": 0x19232D,
    "TEXT": 0xFFFFFF,
    "BORDER": 0x505F69,
    "LINE_BORDER": 0x32414B,
}
DarkGrey9 = {
    "BACKGROUND": 0x36393F,
    "TEXT": 0xDCDDDE,
    "BORDER": 0x202225,
    "LINE_BORDER": 0xB9BBBE,
}
DarkGrey10 = {
    "BACKGROUND": 0x1C1E23,
    "TEXT": 0xCCCDCF,
    "BORDER": 0x313641,
    "LINE_BORDER": 0x2E3D5A,
}
DarkGrey11 = {
    "BACKGROUND": 0x1C1E23,
    "TEXT": 0xCCCDCF,
    "BORDER": 0x313641,
    "LINE_BORDER": 0x313641,
}
DarkGrey12 = {
    "BACKGROUND": 0x1C1E23,
    "TEXT": 0x8B9FDE,
    "BORDER": 0x313641,
    "LINE_BORDER": 0x2E3D5A,
}
DarkGrey13 = {
    "BACKGROUND": 0x1C1E23,
    "TEXT": 0xCCCDCF,
    "BORDER": 0x313641,
    "LINE_BORDER": 0x313641,
}
DarkGrey14 = {
    "BACKGROUND": 0x24292E,
    "TEXT": 0xFAFBFC,
    "BORDER": 0x1D2125,
    "LINE_BORDER": 0x155398,
}
DarkBrown7 = {
    "BACKGROUND": 0x2C2417,
    "TEXT": 0xBAA379,
    "BORDER": 0x392E1C,
    "LINE_BORDER": 0xBAA379,
}
Python = {
    "BACKGROUND": 0x3D7AAB,
    "TEXT": 0xFFDE56,
    "BORDER": 0x295273,
    "LINE_BORDER": 0x295273,
}
