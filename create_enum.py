
import os
from pathlib import Path

target_dir = Path("key_img")
files = sorted([f.name for f in target_dir.glob("*.png")])

print("class KeyImg(Enum):")
for f in files:
    # 変数名として使えるように加工（数字始まりを避け、記号を置換）
    safe_name = f.replace(".png", "").replace("=", "_").replace("-", "_").upper()
    # if safe_name[0].isdigit():
    #     safe_name = "K" + safe_name  # 数字始まりはKをつける例
    print(f'    {safe_name} = "{f}"')