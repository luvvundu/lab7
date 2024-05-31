import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides

class TestGetTriangleType(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(5, 5, 5), 'equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(5, 5, 7), 'isosceles')

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(3, 4, 5), 'nonequilateral')

    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 2, 3)

    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 3)

    def test_sum_of_two_sides_less_than_third(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 3)

if __name__ == '__main__':
    unittest.main()