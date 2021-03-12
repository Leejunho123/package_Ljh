import unittest
import numpy as np
from packageTest_Ljh import Variable


class TestSum(unittest.TestCase):
    def test_datatype(self):
        x = Variable(np.random.rand(10))
        self.x = x