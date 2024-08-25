import pytest
from geo_library.shapes import Square, Triangle  # Adjust the import based on your actual file structure

def test_square_initialization():
    # Test valid initialization
    sq = Square(5)
    assert sq.side_length == 5
    assert sq.area == 25
    assert sq.perimeter == 20

    # Test invalid initialization
    with pytest.raises(ValueError):
        Square(-1)

def test_square_setter():
    sq = Square(5)
    sq.side_length = 10
    assert sq.side_length == 10
    assert sq.area == 100
    assert sq.perimeter == 40

    with pytest.raises(ValueError):
        sq.side_length = -5

def test_square_scaling():
    sq = Square(5)
    sq.scale(2)
    assert sq.side_length == 10
    assert sq.area == 100
    assert sq.perimeter == 40

    with pytest.raises(ValueError):
        sq.scale(-1)

def test_square_comparison():
    sq1 = Square(5)
    sq2 = Square(10)
    assert sq1 < sq2
    assert sq2 > sq1
    assert sq1 == Square(5)

def test_triangle_initialization():
    # Test valid initialization
    tri = Triangle(3, 4, 5)
    assert tri.a == 3
    assert tri.b == 4
    assert tri.c == 5
    assert tri.area == 6
    assert tri.perimeter == 12
    assert tri.is_right_angle() is True

    # Test invalid initialization
    with pytest.raises(ValueError):
        Triangle(1, 1, 3)

def test_triangle_setter():
    tri = Triangle(3, 4, 5)
    tri.a = 6
    assert tri.a == 6
    assert tri.area == pytest.approx(9.92, rel=1e-2)
    assert tri.perimeter == 15

    with pytest.raises(ValueError):
        tri.a = -1

def test_triangle_comparison():
    tri1 = Triangle(3, 4, 5)
    tri2 = Triangle(6, 8, 10)
    tri3 = Triangle(5, 5, 5)
    
    assert tri1 < tri2
    assert tri2 > tri1
    assert tri1 != tri3
    assert tri1 == Triangle(3, 4, 5)

if __name__ == "__main__":
    pytest.main()
