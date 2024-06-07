import pytest
from triangle_class import Triangle, IncorrectTriangleSides

# Позитивные тесты

def test_triangle_type_equilateral():
    triangle = Triangle(5, 5, 5)
    assert triangle.triangle_type() == "equilateral"

def test_triangle_type_isosceles():
    triangle = Triangle(5, 5, 6)
    assert triangle.triangle_type() == "isosceles"

def test_triangle_type_nonequilateral():
    triangle = Triangle(3, 4, 5)
    assert triangle.triangle_type() == "nonequilateral"

def test_triangle_perimeter():
    triangle = Triangle(3, 4, 5)
    assert triangle.perimeter() == 12

# Негативные тесты

def test_invalid_triangle_side_length_zero():
    with pytest.raises(IncorrectTriangleSides):
        triangle = Triangle(0, 4, 5)

def test_invalid_triangle_side_length_negative():
    with pytest.raises(IncorrectTriangleSides):
        triangle = Triangle(3, -4, 5)

def test_invalid_triangle_side_lengths():
    with pytest.raises(IncorrectTriangleSides):
        triangle = Triangle(1, 1, 3)
