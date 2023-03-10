import unittest
import calcProg

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calcProg.add(10,5),15)
        self.assertEqual(calcProg.add(-1,1),0)
        self.assertEqual(calcProg.add(-1,-1),-2)
    
    def test_subtract(self):
        self.assertEqual(calcProg.subtract(10,5),5)
        self.assertEqual(calcProg.subtract(-1,1),-2)
        self.assertEqual(calcProg.subtract(-1,-1),0)
    def test_multiply(self):
        self.assertEqual(calcProg.multiply(10,5),50)
        self.assertEqual(calcProg.multiply(-1,1),-1)
        self.assertEqual(calcProg.multiply(-1,-1),1)

if __name__=='__main__':
    unittest.main()