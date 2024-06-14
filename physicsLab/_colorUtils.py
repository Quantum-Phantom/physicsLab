# -*- coding: utf-8 -*-
from enum import Enum, unique

import colorama
colorama.init(autoreset=True)

@unique
class COLOR(Enum):
    BLACK = colorama.Fore.BLACK
    RED = colorama.Fore.RED
    GREEN = colorama.Fore.GREEN
    YELLOW = colorama.Fore.YELLOW
    BLUE = colorama.Fore.BLUE
    MAGENTA = colorama.Fore.MAGENTA
    CYAN = colorama.Fore.CYAN
    WHITE = colorama.Fore.WHITE

# 打印write_Experiment的信息时是否使用彩色字
_ColorSupport = True

# 打印颜色字
def color_print(msg: str, color: COLOR) -> None:
    if not isinstance(color, COLOR) or not isinstance(msg, str):
        raise TypeError

    global _ColorSupport

    if _ColorSupport:
        print(color.value + msg)
    else:
        print(msg)

# 关闭打印时的color
def close_color_print():
    global _ColorSupport
    _ColorSupport = False