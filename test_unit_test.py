import calc
import unittest



class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2,5), 7)
        
    def test_sub(self):
        self.assertEqual(calc.subtract(5,5), 0)
    
    def test_mult(self):
        self.assertEqual(calc.multiply(10,2), 20000)

    def test_div(self):
        self.assertEqual(calc.divide(50,10), 5)


if __name__ == "__main__":
    unittest.main()