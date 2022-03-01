"""
Test de verificación del modulo.py
"""
import unittest
from modulo import operations

class Test_modulo(unittest.TestCase):
    """Clase que realiza test de forma automática"""

    def testSumatoriaEntera(self):
        """ Sumar bien enteros"""
        self.assertEqual(operations.sumatoria(2,5),7)

    def testSumatoriaEnteraFalla(self):
        """ Sumar bien enteros, pero que falle"""
        self.assertNotEqual(operations.sumatoria(2,5),6)

    def testSumatoriaReal(self):
        """ Sumar números reales con enteros"""
        self.assertEqual(operations.sumatoria(2.5,5),7.5)


if __name__ == "__main__":
    unittest.main()