"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division_1(self):
        assert 10 == calculator.divide(10, 1)

    def test_division_2(self):
        assert 5 == calculator.divide(10, 2)

    def test_division_3(self):
        assert 3 == calculator.divide(10, 3)

    def test_division_4(self):
        assert 2 == calculator.divide(10, 4)

    def test_division_5(self):
        assert 2 == calculator.divide(10, 5)

    def test_division_6(self):
        assert 1 == calculator.divide(10, 6)

    def test_division_7(self):
        assert 1 == calculator.divide(10, 7)

    def test_division_8(self):
        assert 1 == calculator.divide(10, 8)

    def test_division_9(self):
        assert 1 == calculator.divide(10, 9)

    def test_division_10(self):
        assert 1 == calculator.divide(10, 10)

    def test_division_11(self):
        assert 10.0 == calculator.divide(10, 1.0)

    def test_division_12(self):
        assert 5.0 == calculator.divide(10, 2.0)

    def test_division_13(self):
        assert 3.33333333333333 == round(calculator.divide(10, 3.0), 14)

    def test_division_14(self):
        assert 2.5 == calculator.divide(10, 4.0)

    def test_division_15(self):
        assert 2.0 == calculator.divide(10, 5.0)

    def test_division_16(self):
        assert 1.66666666666667 == round(calculator.divide(10, 6.0), 14)

    def test_division_17(self):
        assert 1.42857142857143 == round(calculator.divide(10, 7.0), 14)

    def test_division_18(self):
        assert 1.25 == calculator.divide(10, 8.0)

    def test_division_19(self):
        assert 1.11111111111111 == round(calculator.divide(10, 9.0), 14)

    def test_division_20(self):
        assert 1.0 == calculator.divide(10, 10.0)
