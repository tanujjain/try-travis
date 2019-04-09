from calculator import Calculator


def test_addition():
    mycalculator = Calculator()
    assert mycalculator.myadd(3, 4) == 7


def test_sub():
    mycalculator = Calculator()
    assert mycalculator.mysub(7, 4) == 3