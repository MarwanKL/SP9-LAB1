import unittest
from operaciones import sumar, restar, multiplicar, dividir

class TestOperaciones(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(0, 0), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(5, 3), 15)
        self.assertEqual(multiplicar(10, 5), 50)
        self.assertEqual(multiplicar(0, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(8, 4), 2)
        self.assertEqual(dividir(15, 3), 5)

        # Prueba que se genere una excepción al dividir por cero
        with self.assertRaises(ValueError):
            dividir(6, 0)

if __name__ == '__main__':
    unittest.main()
