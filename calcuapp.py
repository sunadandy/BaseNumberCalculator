import sys

def dec2hex():
    val = sys.argv[1]
    try:
        print(hex(int(val)))
    except:
        # 数値じゃなかったらエラー
        print("input data is invalid")

def dec2bin():
    val = sys.argv[1]
    try:
        print(bin(int(val)))
    except:
        # 数値じゃなかったらエラー
        print("input data is invalid")

def hex2dec():
    val = sys.argv[1]
    try:
        print(int(val, 16))
    except:
        # 数値じゃなかったらエラー
        print("input data is invalid")