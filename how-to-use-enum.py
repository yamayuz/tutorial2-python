# enum(列挙体)
# PythonではEnumというクラスが用意されている
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


if __name__ == '__main__':
    print(Color)
    print(Color(1))
    print(Color.BLUE)