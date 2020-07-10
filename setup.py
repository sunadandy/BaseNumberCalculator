from setuptools import setup

setup(
    name="BaseNumberCalcurater",
    version="0.0.1",
    author="sunadandy",
    entry_points={
        "console_scripts": [
            "dec2hex = calcuapp:dec2hex",
            "dec2bin = calcuapp:dec2bin",
            "hex2dec = calcuapp:hex2dec",
        ]
    }
)