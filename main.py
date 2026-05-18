from enum import Enum
from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont
# 画像フォルダのベースパスを定義
import os

PAIRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(PAIRENT_DIR,"key_img")
IMG_DIR = Path(IMG_DIR)

class KeyImg(Enum):
    PLUS = "+.png"
    F1 = "001=F1.png"
    F2 = "002=F2.png"
    F3 = "003=F3.png"
    F4 = "004=F4.png"
    F5 = "005=F5.png"
    F6 = "006=F6.png"
    F7 = "007=F7.png"
    F8 = "008=F8.png"
    F9 = "009=F9.png"
    F10 = "010=F10.png"
    F11 = "011=F11.png"
    F12 = "012=F12.png"

    ZEN_HAN = "100=zen_han.png"

    N_1 = "101=1.png"
    N_2 = "102=2.png"
    N_3 = "103=3.png"
    N_4 = "104=4.png"
    N_5 = "105=5.png"
    N_6 = "106=6.png"
    N_7 = "107=7.png"
    N_8 = "108=8.png"
    N_9 = "109=9.png"
    N_0 = "110=0.png"

    MINUS = "111=-.png"
    HAT = "112=^.png"
    EN_MARK = "113=en_mark.png"
    BS = "114=bs.png"
    TAB = "200=tab.png"

    Q = "201=Q.png"
    W = "202=w.png"
    E = "203=E.png"
    R = "204=R.png"
    T = "205=T.png"
    Y = "206=Y.png"
    U = "207=U.png"
    I = "208=I.png"
    O = "209=O.png"
    P = "210=P.png"

    AT_MARK = "211=at_mark.png"
    LEFT_BRACKET = "212=[.png"
    ENTER = "213_enter.png"
    SPACE = "space.png"

    A = "301=A.png"
    S = "302=S.png"
    D = "303=D.png"
    F = "304=F.png"
    G = "305=G.png"
    H = "306=H.png"
    J = "307=J.png"
    K = "308=K.png"
    L = "309=L.png"

    SEMICOLON = "310=semicolon.png"
    COLON = "311=colon.png"
    RIGHT_BRACKET = "312=].png"

    Z = "401=Z.png"
    X = "402=X.png"
    C = "403=C.png"
    V = "404=V.png"
    B = "405=B.png"
    N = "406=N.png"
    M = "407=M.png"

    COMMA = "408=,.png"
    DOT = "409=..png"
    SLASH = "410=slash.png"
    UNDER_BAR = "411=_.png"
    ALT = "alt.png"
    BLANK = "blank.png"
    CTRL = "ctrl.png"
    DEL = "del.png"
    DOWN = "down.png"
    END = "end.png"
    ESC = "esc.png"
    HOME = "home.png"
    INS = "ins.png"
    LEFT = "left.png"

    NUM_0 = "num=0.png"
    NUM_1 = "num=1.png"
    NUM_2 = "num=2.png"
    NUM_3 = "num=3.png"
    NUM_4 = "num=4.png"
    NUM_5 = "num=5.png"
    NUM_6 = "num=6.png"
    NUM_7 = "num=7.png"
    NUM_8 = "num=8.png"
    NUM_9 = "num=9.png"
    NUM_DIV = "num=div.png"
    NUM_DOT = "num=dot.png"
    NUM_LOCK = "num=lock.png"
    NUM_MIN = "num=min.png"
    NUM_MULTI = "num=multi.png"
    NUM_PLUS = "+.png"

    PAGE_DOWN = "page_down.png"
    PAGE_UP = "page_up.png"
    RIGHT = "right.png"
    SHIFT = "shift.png"
    UP = "up.png"

    # 特殊表示 word メイリオ18pt スクショ ブランクと組み合わせて作製
    KAKUDAI = "kakudai.png"
    SYUKUSYOU = "syukusyou.png"
    ALL = "all.png"
    SEARCH = "search.png"
    MODOSU = "modosu_undo.png"
    CUT = "cut.png"
    COPY = "copy.png"
    PASTE = "paste.png"

    # マウス
    BACKWARD = "backward.png"
    FORWARD = "forward.png"
    CLICK_LEFT = "click_left.png"
    CLICK_CENTER = "click_center.png"
    CLICK_RIGHT = "click_right.png"

    # アプリケーション
    EXCEL = "excel.png"
    PYCHARM = "pycharm.png"

    # PyCharm
    ERROR_MOVE = "error_move.png"
    RENAME = "rename.png"
    EXE = "exe.png"
    EXPLAIN = "explain.png"
    BOOK_MARK = "bookmark.png"
    FILE = "latest_file.png"
    WORD = "word.png"
    REPLACE = "replace.png"
    MENU = "menu.png"
    SAVE = "save.png"
    FUKUSEI = "fukusei.png"
    FUNC = "func.png"
    COMMENT = "comment.png"

# ==========================================
# 1. Layout（座標データ）
# キーの位置IDに対する、X座標, Y座標, 回転角度
# ※この値は画像編集ソフト等で事前に測っておきます
# ==========================================

left_x = 5
right_x = 695


keyboard_layout = {
    # 左手1行目
    "Left_Row1_Col1": {"x": left_x +80*0, "y": 30+80*0,  "angle": 0},
    "Left_Row1_Col2": {"x": left_x +80*1, "y": 30+80*0,  "angle": 0},
    "Left_Row1_Col3": {"x": left_x +80*2, "y": 15+80*0,  "angle": 0},
    "Left_Row1_Col4": {"x": left_x +80*3, "y": 10+80*0,  "angle": 0},
    "Left_Row1_Col5": {"x": left_x +80*4, "y": 15+80*0,  "angle": 0},
    "Left_Row1_Col6": {"x": left_x +80*5, "y": 25+80*0,  "angle": 0},

    # 左手2行目
    "Left_Row2_Col1": {"x": left_x + 80 * 0, "y": 30+80*1, "angle": 0},
    "Left_Row2_Col2": {"x": left_x + 80 * 1, "y": 30+80*1, "angle": 0},
    "Left_Row2_Col3": {"x": left_x + 80 * 2, "y": 15+80*1, "angle": 0},
    "Left_Row2_Col4": {"x": left_x + 80 * 3, "y": 10+80*1, "angle": 0},
    "Left_Row2_Col5": {"x": left_x + 80 * 4, "y": 15+80*1, "angle": 0},
    "Left_Row2_Col6": {"x": left_x + 80 * 5, "y": 25+80*1, "angle": 0},

    # 左手3行目
    "Left_Row3_Col1": {"x": left_x + 80 * 0, "y": 30+80*2, "angle": 0},
    "Left_Row3_Col2": {"x": left_x + 80 * 1, "y": 30+80*2, "angle": 0},
    "Left_Row3_Col3": {"x": left_x + 80 * 2, "y": 15+80*2, "angle": 0},
    "Left_Row3_Col4": {"x": left_x + 80 * 3, "y": 10+80*2, "angle": 0},
    "Left_Row3_Col5": {"x": left_x + 80 * 4, "y": 15+80*2, "angle": 0},
    "Left_Row3_Col6": {"x": left_x + 80 * 5, "y": 25+80*2, "angle": 0},

    # 左手4行目
    "Left_Row4_Col1": {"x": left_x + 80 * 0, "y": 30+80*3, "angle": 0},
    "Left_Row4_Col2": {"x": left_x + 80 * 1, "y": 30+80*3, "angle": 0},
    "Left_Row4_Col3": {"x": left_x + 80 * 2, "y": 15+80*3, "angle": 0},
    "Left_Row4_Col4": {"x": left_x + 80 * 3, "y": 10+80*3, "angle": 0},
    "Left_Row4_Col5": {"x": left_x + 80 * 4, "y": 15+80*3, "angle": 0},
    "Left_Row4_Col6": {"x": left_x + 80 * 5, "y": 25+80*3, "angle": 0},

    # 右手1行目
    "Right_Row1_Col6": {"x": right_x+ 80 * 5,  "y": 30+80*0, "angle": 0},
    "Right_Row1_Col5": {"x": right_x+ 80 * 4,  "y": 30+80*0, "angle": 0},
    "Right_Row1_Col4": {"x": right_x+ 80 * 3,  "y": 15+80*0, "angle": 0},
    "Right_Row1_Col3": {"x": right_x+ 80 * 2,  "y": 10+80*0, "angle": 0},
    "Right_Row1_Col2": {"x": right_x+ 80 * 1,  "y": 15+80*0, "angle": 0},
    "Right_Row1_Col1": {"x": right_x+ 80 * 0,  "y": 25+80*0, "angle": 0},

    # 右手2行目
    "Right_Row2_Col6": {"x": right_x + 80 * 5, "y": 30 + 80 * 1, "angle": 0},
    "Right_Row2_Col5": {"x": right_x + 80 * 4, "y": 30 + 80 * 1, "angle": 0},
    "Right_Row2_Col4": {"x": right_x + 80 * 3, "y": 15 + 80 * 1, "angle": 0},
    "Right_Row2_Col3": {"x": right_x + 80 * 2, "y": 10 + 80 * 1, "angle": 0},
    "Right_Row2_Col2": {"x": right_x + 80 * 1, "y": 15 + 80 * 1, "angle": 0},
    "Right_Row2_Col1": {"x": right_x + 80 * 0, "y": 25 + 80 * 1, "angle": 0},

    # 右手3行目
    "Right_Row3_Col6": {"x": right_x + 80 * 5, "y": 30 + 80 * 2, "angle": 0},
    "Right_Row3_Col5": {"x": right_x + 80 * 4, "y": 30 + 80 * 2, "angle": 0},
    "Right_Row3_Col4": {"x": right_x + 80 * 3, "y": 15 + 80 * 2, "angle": 0},
    "Right_Row3_Col3": {"x": right_x + 80 * 2, "y": 10 + 80 * 2, "angle": 0},
    "Right_Row3_Col2": {"x": right_x + 80 * 1, "y": 15 + 80 * 2, "angle": 0},
    "Right_Row3_Col1": {"x": right_x + 80 * 0, "y": 25 + 80 * 2, "angle": 0},

    # 右手4行目
    "Right_Row4_Col6": {"x": right_x + 80 * 5, "y": 30 + 80 * 3, "angle": 0},
    "Right_Row4_Col5": {"x": right_x + 80 * 4, "y": 30 + 80 * 3, "angle": 0},
    "Right_Row4_Col4": {"x": right_x + 80 * 3, "y": 15 + 80 * 3, "angle": 0},
    "Right_Row4_Col3": {"x": right_x + 80 * 2, "y": 10 + 80 * 3, "angle": 0},
    "Right_Row4_Col2": {"x": right_x + 80 * 1, "y": 15 + 80 * 3, "angle": 0},
    "Right_Row4_Col1": {"x": right_x + 80 * 0, "y": 25 + 80 * 3, "angle": 0},

    # 左親指　上の段　左から
    "Thumb_Left_1": {"x": 260, "y": 340, "angle": -30},
    "Thumb_Left_2": {"x": 330, "y": 380, "angle": -30},
    "Thumb_Left_3": {"x": 400, "y": 420, "angle": -30},

    # 左親指　下の段　左から
    "Thumb_Left_4":   {"x": 280, "y": 450, "angle": -30},
    "Thumb_Left_5":   {"x": 350, "y": 490, "angle": -30},


    # 右親指　上の段　右から
    "Thumb_Right_1": {"x": right_x+70, "y": 335, "angle": 35},
    "Thumb_Right_2": {"x": right_x, "y": 380, "angle": 35},

    # 右親指　下の段
    "Thumb_Right_3": {"x": right_x+45, "y": 450, "angle": 35},

}

# ==========================================
# 2. Keymap（配列パターンデータ）
# パターンごとに、どの位置IDにどの画像ファイルを入れるか指定
# ==========================================



patterns = [
    {
        "pattern_name": "f13",
        "display_name": "大西配列",
        "keys": {
            # -------------------------------------
            # 左手1行目
            "Left_Row1_Col1": str(IMG_DIR / KeyImg.ESC.value),
            "Left_Row1_Col2": str(IMG_DIR / KeyImg.N_1.value),
            "Left_Row1_Col3": str(IMG_DIR / KeyImg.N_2.value),
            "Left_Row1_Col4": str(IMG_DIR / KeyImg.N_3.value),
            "Left_Row1_Col5": str(IMG_DIR / KeyImg.N_4.value),
            "Left_Row1_Col6": str(IMG_DIR / KeyImg.N_5.value),

            # 右手1行目
            "Right_Row1_Col1": str(IMG_DIR / KeyImg.N_6.value),
            "Right_Row1_Col2": str(IMG_DIR / KeyImg.N_7.value),
            "Right_Row1_Col3": str(IMG_DIR / KeyImg.N_8.value),
            "Right_Row1_Col4": str(IMG_DIR / KeyImg.N_9.value),
            "Right_Row1_Col5": str(IMG_DIR / KeyImg.N_0.value),
            "Right_Row1_Col6": str(IMG_DIR / KeyImg.LEFT_BRACKET.value),

            # -------------------------------------
            # 左手2行目
            "Left_Row2_Col1": str(IMG_DIR / KeyImg.HAT.value),
            "Left_Row2_Col2": str(IMG_DIR / KeyImg.Q.value),
            "Left_Row2_Col3": str(IMG_DIR / KeyImg.L.value),
            "Left_Row2_Col4": str(IMG_DIR / KeyImg.U.value),
            "Left_Row2_Col5": str(IMG_DIR / KeyImg.COMMA.value),
            "Left_Row2_Col6": str(IMG_DIR / KeyImg.DOT.value),

            # 右手2行目
            "Right_Row2_Col1": str(IMG_DIR / KeyImg.UNDER_BAR.value),
            "Right_Row2_Col2": str(IMG_DIR / KeyImg.W.value),
            "Right_Row2_Col3": str(IMG_DIR / KeyImg.R.value),
            "Right_Row2_Col4": str(IMG_DIR / KeyImg.Y.value),
            "Right_Row2_Col5": str(IMG_DIR / KeyImg.P.value),
            "Right_Row2_Col6": str(IMG_DIR / KeyImg.RIGHT_BRACKET.value),

            # -------------------------------------
            # 左手3行目
            "Left_Row3_Col1": str(IMG_DIR / KeyImg.SEMICOLON.value),
            "Left_Row3_Col2": str(IMG_DIR / KeyImg.E.value),
            "Left_Row3_Col3": str(IMG_DIR / KeyImg.I.value),
            "Left_Row3_Col4": str(IMG_DIR / KeyImg.A.value),
            "Left_Row3_Col5": str(IMG_DIR / KeyImg.O.value),
            "Left_Row3_Col6": str(IMG_DIR / KeyImg.F.value),

            # 右手3行目
            "Right_Row3_Col1": str(IMG_DIR / KeyImg.K.value),
            "Right_Row3_Col2": str(IMG_DIR / KeyImg.T.value),
            "Right_Row3_Col3": str(IMG_DIR / KeyImg.N.value),

            "Right_Row3_Col4": str(IMG_DIR / KeyImg.S.value),
            "Right_Row3_Col5": str(IMG_DIR / KeyImg.H.value),
            "Right_Row3_Col6": str(IMG_DIR / KeyImg.COLON.value),

            # -------------------------------------
            # 左手4行目
            "Left_Row4_Col1": str(IMG_DIR / KeyImg.EN_MARK.value),
            "Left_Row4_Col2": str(IMG_DIR / KeyImg.Z.value),
            "Left_Row4_Col3": str(IMG_DIR / KeyImg.X.value),
            "Left_Row4_Col4": str(IMG_DIR / KeyImg.C.value),
            "Left_Row4_Col5": str(IMG_DIR / KeyImg.V.value),
            "Left_Row4_Col6": str(IMG_DIR / KeyImg.MINUS.value),

            # 右手4行目
            "Right_Row4_Col1": str(IMG_DIR / KeyImg.G.value),
            "Right_Row4_Col2": str(IMG_DIR / KeyImg.D.value),
            "Right_Row4_Col3": str(IMG_DIR / KeyImg.M.value),
            "Right_Row4_Col4": str(IMG_DIR / KeyImg.J.value),
            "Right_Row4_Col5": str(IMG_DIR / KeyImg.B.value),
            "Right_Row4_Col6": str(IMG_DIR / KeyImg.SLASH.value),

            # -------------------------------------
            "Thumb_Left_1":   str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_2":   str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_3":   str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Left_4":   str(IMG_DIR / KeyImg.BS.value),
            "Thumb_Left_5":   str(IMG_DIR / KeyImg.SPACE.value),


            "Thumb_Right_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_2": str(IMG_DIR / KeyImg.CTRL.value),

            "Thumb_Right_3": str(IMG_DIR / KeyImg.SHIFT.value),
        }
    },

    {
        "pattern_name": "f14",
        "display_name": "マウスモード",
        "keys": {
            # -------------------------------------
            # 左手1行目
            "Left_Row1_Col1": str(IMG_DIR / KeyImg.ESC.value),
            "Left_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col3": str(IMG_DIR / KeyImg.F2.value),
            "Left_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手1行目
            "Right_Row1_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col2": str(IMG_DIR / KeyImg.SYUKUSYOU.value),
            "Right_Row1_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col4": str(IMG_DIR / KeyImg.KAKUDAI.value),
            "Right_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手2行目
            "Left_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col4": str(IMG_DIR / KeyImg.TAB.value),
            "Left_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手2行目
            "Right_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col2": str(IMG_DIR / KeyImg.PAGE_DOWN.value),
            "Right_Row2_Col3": str(IMG_DIR / KeyImg.UP.value),
            "Right_Row2_Col4": str(IMG_DIR / KeyImg.PAGE_UP.value),
            "Right_Row2_Col5": str(IMG_DIR / KeyImg.DEL.value),
            "Right_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手3行目
            "Left_Row3_Col1": str(IMG_DIR / KeyImg.ALT.value),
            "Left_Row3_Col2": str(IMG_DIR / KeyImg.CTRL.value),
            "Left_Row3_Col3": str(IMG_DIR / KeyImg.SHIFT.value),
            "Left_Row3_Col4": str(IMG_DIR / KeyImg.ALL.value),
            "Left_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col6": str(IMG_DIR / KeyImg.SEARCH.value),

            # 右手3行目
            "Right_Row3_Col1": str(IMG_DIR / KeyImg.HOME.value),
            "Right_Row3_Col2": str(IMG_DIR / KeyImg.LEFT.value),
            "Right_Row3_Col3": str(IMG_DIR / KeyImg.DOWN.value),
            "Right_Row3_Col4": str(IMG_DIR / KeyImg.RIGHT.value),
            "Right_Row3_Col5": str(IMG_DIR / KeyImg.END.value),
            "Right_Row3_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手4行目
            "Left_Row4_Col1": str(IMG_DIR / KeyImg.SHIFT.value),
            "Left_Row4_Col2": str(IMG_DIR / KeyImg.MODOSU.value),
            "Left_Row4_Col3": str(IMG_DIR / KeyImg.CUT.value),
            "Left_Row4_Col4": str(IMG_DIR / KeyImg.COPY.value),
            "Left_Row4_Col5": str(IMG_DIR / KeyImg.PASTE.value),
            "Left_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手4行目
            "Right_Row4_Col1": str(IMG_DIR / KeyImg.BACKWARD.value),
            "Right_Row4_Col2": str(IMG_DIR / KeyImg.CLICK_LEFT.value),
            "Right_Row4_Col3": str(IMG_DIR / KeyImg.CLICK_CENTER.value),
            "Right_Row4_Col4": str(IMG_DIR / KeyImg.CLICK_RIGHT.value),
            "Right_Row4_Col5": str(IMG_DIR / KeyImg.FORWARD.value),
            "Right_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            "Thumb_Left_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_2": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_3": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Left_4": str(IMG_DIR / KeyImg.BS.value),
            "Thumb_Left_5": str(IMG_DIR / KeyImg.ENTER.value),

            "Thumb_Right_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_2": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Right_3": str(IMG_DIR / KeyImg.BLANK.value),
        }
    },
    {
        "pattern_name": "f15" ,
        "display_name": "テンキーモード",
        "keys": {
            # -------------------------------------
            # 左手1行目
            "Left_Row1_Col1": str(IMG_DIR / KeyImg.ESC.value),
            "Left_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手1行目
            "Right_Row1_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col2": str(IMG_DIR / KeyImg.NUM_PLUS.value),
            "Right_Row1_Col3": str(IMG_DIR / KeyImg.NUM_MIN.value),
            "Right_Row1_Col4": str(IMG_DIR / KeyImg.NUM_MULTI.value),
            "Right_Row1_Col5": str(IMG_DIR / KeyImg.NUM_DIV.value),
            "Right_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手2行目
            "Left_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col4": str(IMG_DIR / KeyImg.TAB.value),
            "Left_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手2行目
            "Right_Row2_Col1": str(IMG_DIR / KeyImg.UNDER_BAR.value),
            "Right_Row2_Col2": str(IMG_DIR / KeyImg.NUM_7.value),
            "Right_Row2_Col3": str(IMG_DIR / KeyImg.NUM_8.value),
            "Right_Row2_Col4": str(IMG_DIR / KeyImg.NUM_9.value),
            "Right_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手3行目
            "Left_Row3_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手3行目
            "Right_Row3_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col2": str(IMG_DIR / KeyImg.NUM_4.value),
            "Right_Row3_Col3": str(IMG_DIR / KeyImg.NUM_5.value),
            "Right_Row3_Col4": str(IMG_DIR / KeyImg.NUM_6.value),
            "Right_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col6": str(IMG_DIR / KeyImg.ENTER.value),

            # -------------------------------------
            # 左手4行目
            "Left_Row4_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手4行目
            "Right_Row4_Col1": str(IMG_DIR / KeyImg.NUM_0.value),
            "Right_Row4_Col2": str(IMG_DIR / KeyImg.NUM_1.value),
            "Right_Row4_Col3": str(IMG_DIR / KeyImg.NUM_2.value),
            "Right_Row4_Col4": str(IMG_DIR / KeyImg.NUM_3.value),
            "Right_Row4_Col5": str(IMG_DIR / KeyImg.NUM_DOT.value),
            "Right_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            "Thumb_Left_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_2": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_3": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Left_4": str(IMG_DIR / KeyImg.BS.value),
            "Thumb_Left_5": str(IMG_DIR / KeyImg.SPACE.value),

            "Thumb_Right_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_2": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Right_3": str(IMG_DIR / KeyImg.BLANK.value),
        }
    },
    {
        "pattern_name": "f16",
        "display_name": "アプリモード",
        "keys": {
            # -------------------------------------
            # 左手1行目
            "Left_Row1_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手1行目
            "Right_Row1_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手2行目
            "Left_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手2行目
            "Right_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col5": str(IMG_DIR / KeyImg.PYCHARM.value),
            "Right_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手3行目
            "Left_Row3_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col2": str(IMG_DIR / KeyImg.EXCEL.value),
            "Left_Row3_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手3行目
            "Right_Row3_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手4行目
            "Left_Row4_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手4行目
            "Right_Row4_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            "Thumb_Left_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_2": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_3": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Left_4": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_5": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Right_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_2": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Right_3": str(IMG_DIR / KeyImg.BLANK.value),
        }
    },
    {
        "pattern_name": "f17",
        "display_name": "エクセルモード",
        "keys": {
            # -------------------------------------
            # 左手1行目
            "Left_Row1_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手1行目
            "Right_Row1_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手2行目
            "Left_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手2行目
            "Right_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手3行目
            "Left_Row3_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手3行目
            "Right_Row3_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手4行目
            "Left_Row4_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手4行目
            "Right_Row4_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            "Thumb_Left_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_2": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_3": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_4": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_5": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Right_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_2": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_3": str(IMG_DIR / KeyImg.BLANK.value),
        }
    },
    {
        "pattern_name": "f18",
        "display_name": "Pycharm",
        "keys": {
            # -------------------------------------
            # 左手1行目
            "Left_Row1_Col1": str(IMG_DIR / KeyImg.ESC.value),
            "Left_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col3": str(IMG_DIR / KeyImg.ERROR_MOVE.value),
            "Left_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手1行目
            "Right_Row1_Col1": str(IMG_DIR / KeyImg.RENAME.value),
            "Right_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col5": str(IMG_DIR / KeyImg.EXE.value),
            "Right_Row1_Col6": str(IMG_DIR / KeyImg.BOOK_MARK.value),

            # -------------------------------------
            # 左手2行目
            "Left_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col2": str(IMG_DIR / KeyImg.EXPLAIN.value),
            "Left_Row2_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col4": str(IMG_DIR / KeyImg.TAB.value),
            "Left_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手2行目
            "Right_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col2": str(IMG_DIR / KeyImg.WORD.value),
            "Right_Row2_Col3": str(IMG_DIR / KeyImg.REPLACE.value),
            "Right_Row2_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手3行目
            "Left_Row3_Col1": str(IMG_DIR / KeyImg.MENU.value),
            "Left_Row3_Col2": str(IMG_DIR / KeyImg.FILE.value),
            "Left_Row3_Col3": str(IMG_DIR / KeyImg.SHIFT.value),
            "Left_Row3_Col4": str(IMG_DIR / KeyImg.ALL.value),
            "Left_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col6": str(IMG_DIR / KeyImg.SEARCH.value),

            # 右手3行目
            "Right_Row3_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col4": str(IMG_DIR / KeyImg.SAVE.value),
            "Right_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row3_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手4行目
            "Left_Row4_Col1": str(IMG_DIR / KeyImg.SHIFT.value),
            "Left_Row4_Col2": str(IMG_DIR / KeyImg.MODOSU.value),
            "Left_Row4_Col3": str(IMG_DIR / KeyImg.CUT.value),
            "Left_Row4_Col4": str(IMG_DIR / KeyImg.COPY.value),
            "Left_Row4_Col5": str(IMG_DIR / KeyImg.PASTE.value),
            "Left_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手4行目
            "Right_Row4_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col2": str(IMG_DIR / KeyImg.CLICK_LEFT.value),
            "Right_Row4_Col3": str(IMG_DIR / KeyImg.CLICK_CENTER.value),
            "Right_Row4_Col4": str(IMG_DIR / KeyImg.CLICK_RIGHT.value),
            "Right_Row4_Col5": str(IMG_DIR / KeyImg.FUNC.value),
            "Right_Row4_Col6": str(IMG_DIR / KeyImg.COMMENT.value),

            # -------------------------------------
            "Thumb_Left_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_2": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_3": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_4": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_5": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Right_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_2": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_3": str(IMG_DIR / KeyImg.BLANK.value),
        }
    },
 {
        "pattern_name": "f23",
        "display_name": "編集モード",
        "keys": {
            # -------------------------------------
            # 左手1行目
            "Left_Row1_Col1": str(IMG_DIR / KeyImg.ESC.value),
            "Left_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col3": str(IMG_DIR / KeyImg.F2.value),
            "Left_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手1行目
            "Right_Row1_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col3": str(IMG_DIR / KeyImg.F8.value),
            "Right_Row1_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row1_Col5": str(IMG_DIR / KeyImg.F10.value),
            "Right_Row1_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手2行目
            "Left_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col2": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col3": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col4": str(IMG_DIR / KeyImg.TAB.value),
            "Left_Row2_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手2行目
            "Right_Row2_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row2_Col2": str(IMG_DIR / KeyImg.PAGE_DOWN.value),
            "Right_Row2_Col3": str(IMG_DIR / KeyImg.UP.value),
            "Right_Row2_Col4": str(IMG_DIR / KeyImg.PAGE_UP.value),
            "Right_Row2_Col5": str(IMG_DIR / KeyImg.DEL.value),
            "Right_Row2_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手3行目
            "Left_Row3_Col1": str(IMG_DIR / KeyImg.ALT.value),
            "Left_Row3_Col2": str(IMG_DIR / KeyImg.CTRL.value),
            "Left_Row3_Col3": str(IMG_DIR / KeyImg.SHIFT.value),
            "Left_Row3_Col4": str(IMG_DIR / KeyImg.ALL.value),
            "Left_Row3_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Left_Row3_Col6": str(IMG_DIR / KeyImg.SEARCH.value),

            # 右手3行目
            "Right_Row3_Col1": str(IMG_DIR / KeyImg.HOME.value),
            "Right_Row3_Col2": str(IMG_DIR / KeyImg.LEFT.value),
            "Right_Row3_Col3": str(IMG_DIR / KeyImg.DOWN.value),
            "Right_Row3_Col4": str(IMG_DIR / KeyImg.RIGHT.value),
            "Right_Row3_Col5": str(IMG_DIR / KeyImg.END.value),
            "Right_Row3_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # -------------------------------------
            # 左手4行目
            "Left_Row4_Col1": str(IMG_DIR / KeyImg.SHIFT.value),
            "Left_Row4_Col2": str(IMG_DIR / KeyImg.MODOSU.value),
            "Left_Row4_Col3": str(IMG_DIR / KeyImg.CUT.value),
            "Left_Row4_Col4": str(IMG_DIR / KeyImg.COPY.value),
            "Left_Row4_Col5": str(IMG_DIR / KeyImg.PASTE.value),
            "Left_Row4_Col6": str(IMG_DIR / KeyImg.BLANK.value),

            # 右手4行目
            "Right_Row4_Col1": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col2": str(IMG_DIR / KeyImg.CLICK_LEFT.value),
            "Right_Row4_Col3": str(IMG_DIR / KeyImg.TAB.value),
            "Right_Row4_Col4": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col5": str(IMG_DIR / KeyImg.BLANK.value),
            "Right_Row4_Col6": str(IMG_DIR / KeyImg.SLASH.value),

            # -------------------------------------
            "Thumb_Left_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_2": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Left_3": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Left_4": str(IMG_DIR / KeyImg.BS.value),
            "Thumb_Left_5": str(IMG_DIR / KeyImg.SPACE.value),

            "Thumb_Right_1": str(IMG_DIR / KeyImg.BLANK.value),
            "Thumb_Right_2": str(IMG_DIR / KeyImg.BLANK.value),

            "Thumb_Right_3": str(IMG_DIR / KeyImg.BLANK.value),
        }
    },

]

from PIL import Image
import os


def generate_keyboard_image(base_img_path, layout_data, keymap_data, output_dir):
    """
    ベース画像にキー画像を合成して保存する関数
    """
    pattern_name = keymap_data["pattern_name"]
    keys = keymap_data["keys"]
    text = keymap_data.get("display_name", pattern_name)

    # 1. ベース画像を開く（背景透過を維持するためRGBAで開く）
    base_img = Image.open(base_img_path).convert("RGBA")

    # 2. 各キー画像を配置していく
    for position_id, key_img_path in keys.items():
        if position_id not in layout_data:
            print(f"Warning: {position_id} の座標データがありません。スキップします。")
            continue

        if not os.path.exists(key_img_path):
            print(f"Warning: 画像 {key_img_path} が見つかりません。スキップします。")
            continue

        # 座標と角度を取得
        pos_info = layout_data[position_id]
        x, y = pos_info["x"], pos_info["y"]
        angle = pos_info.get("angle", 0)

        # キー画像を開く
        key_img = Image.open(key_img_path).convert("RGBA")

        # 必要に応じて回転させる (expand=Trueで回転によってはみ出た部分が切れないようにする)
        if angle != 0:
            key_img = key_img.rotate(angle, expand=True, resample=Image.BICUBIC)
            # ※注意: 回転させると画像のサイズ(Bounding Box)が変わるため、
            # 厳密な中央配置をする場合は x, y 座標の微調整計算が別途必要になる場合があります。

        # ベース画像に貼り付け (第3引数のkey_imgは透過(Alpha)マスクとして使用)
        base_img.paste(key_img, (x, y), key_img)

    # 右下に配列名を描画
    draw = ImageDraw.Draw(base_img)

    font_size = 36
    try:
        font = ImageFont.truetype("C:/Windows/Fonts/meiryo.ttc", font_size)
    except:
        font = ImageFont.load_default()

    text = keymap_data.get("display_name", pattern_name)

    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    margin = 30
    x = base_img.width - text_width - margin
    y = base_img.height - text_height - margin

    draw.text((x, y), text, fill=(0, 0, 0, 255), font=font)

    # 3. 保存
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{pattern_name}.png")
    base_img.save(output_path, "PNG")
    print(f"Saved: {output_path}")


# ==========================================
# 実行部分（ループ処理）
# ==========================================
if __name__ == "__main__":
    # base_image = "bk_black.png"
    base_image = "bk_white.png"
    output_directory = "output_images"

    # 用意したパターンを順番に処理して一気に書き出す
    for pattern in patterns:
        generate_keyboard_image(base_image, keyboard_layout, pattern, output_directory)




