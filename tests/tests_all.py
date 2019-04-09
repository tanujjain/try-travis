from calculator import Calculator


def test_addition():
    mycalculator = Calculator()
    assert mycalculator.myadd(3, 4) == 7