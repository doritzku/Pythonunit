import unittest
import calc 


class TestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1,2),3)
        self.assertEqual(calc.add(3,-2),1)
        self.assertEqual(calc.add(4,2),6)
        self.assertEqual(calc.add(2,2),4)

    def test_div(self):
        self.assertEqual(calc.div(4,2),2)
        self.assertEqual(calc.div(6,2),3)




