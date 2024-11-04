import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) # actual output vs expected output

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(-2, 1), -3)

    def test_sub_zero(self):
        self.assertEqual(self.calc.subtract(1, 0), 1)

    def test_mul_negative(self):
        self.assertEqual(self.calc.multiply(2, -3), -6)

    def test_mul_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_div_negative(self):
        self.assertEqual(self.calc.divide(8, -2), -4)

    def test_div_zero(self):
        self.assertEqual(self.calc.divide(2, 0), "Any numbers can't be divided by zero")

    def test_mod_negative(self):
        self.assertEqual(self.calc.modulo(10, -3), -1)

    def test_mod_zero(self):
        self.assertEqual(self.calc.modulo(10, 0), "You can't divide any numbers with zero")

if __name__ == '__main__':
    unittest.main()
