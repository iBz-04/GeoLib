import math




## FOR SQUARES
class Square:
    def __init__(self, side_length):
        """
        Initialize a Square with a given side length.
        
        Parameters:
        - side_length: Length of the sides of the square. Must be positive.
        """
        self._side_length = None
        self.side_length = side_length  # Use setter to validate

    @property
    def side_length(self):
        """
        Get the length of the side of the square.
        """
        return self._side_length

    @side_length.setter
    def side_length(self, value):
        """
        Set the length of the side of the square. Must be positive.
        
        Parameters:
        - value: New length of the side. Must be positive.
        
        Raises:
        - ValueError: If the length is not positive.
        """
        if value <= 0:
            raise ValueError("Side length must be positive.")
        self._side_length = value

    @property
    def area(self):
        """
        Calculate the area of the square.
        
        Returns:
        - The area of the square.
        """
        return self.side_length ** 2

    @property
    def perimeter(self):
        """
        Calculate the perimeter of the square.
        
        Returns:
        - The perimeter of the square.
        """
        return 4 * self.side_length

    def __repr__(self):
        """
        Return a string representation of the square.
        
        Returns:
        - A string describing the square.
        """
        return f"Square(side_length={self.side_length})"

    def scale(self, factor):
        """
        Scale the square by a given factor.
        
        Parameters:
        - factor: Scaling factor. Must be positive.
        
        Raises:
        - ValueError: If the scaling factor is not positive.
        """
        if factor <= 0:
            raise ValueError("Scale factor must be positive.")
        self.side_length *= factor

    def __eq__(self, other):
        """
        Check if this square is equal to another square.
        
        Parameters:
        - other: Another square to compare with.
        
        Returns:
        - True if the squares are equal, False otherwise.
        """
        return isinstance(other, Square) and self.side_length == other.side_length

    def __lt__(self, other):
        """
        Compare this square with another square by side length.
        
        Parameters:
        - other: Another square to compare with.
        
        Returns:
        - True if this square is smaller than the other square, False otherwise.
        """
        if isinstance(other, Square):
            return self.side_length < other.side_length
        return NotImplemented










## FOR TRIANGLES 
class Triangle:
    def __init__(self, a, b, c):
        """
        Initialize a Triangle with three side lengths.
        
        Parameters:
        - a: Length of the first side. Must be positive.
        - b: Length of the second side. Must be positive.
        - c: Length of the third side. Must be positive.
        
        Raises:
        - ValueError: If any side length is not positive or if the sides do not form a triangle.
        """
        self._a = self._b = self._c = None
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        """
        Get the length of the first side of the triangle.
        """
        return self._a

    @a.setter
    def a(self, value):
        """
        Set the length of the first side of the triangle. Must be positive.
        
        Parameters:
        - value: New length of the first side. Must be positive.
        
        Raises:
        - ValueError: If the length is not positive or if the sides do not form a triangle.
        """
        if value <= 0:
            raise ValueError("Side length must be positive.")
        self._a = value
        self._validate_triangle()

    @property
    def b(self):
        """
        Get the length of the second side of the triangle.
        """
        return self._b

    @b.setter
    def b(self, value):
        """
        Set the length of the second side of the triangle. Must be positive.
        
        Parameters:
        - value: New length of the second side. Must be positive.
        
        Raises:
        - ValueError: If the length is not positive or if the sides do not form a triangle.
        """
        if value <= 0:
            raise ValueError("Side length must be positive.")
        self._b = value
        self._validate_triangle()

    @property
    def c(self):
        """
        Get the length of the third side of the triangle.
        """
        return self._c

    @c.setter
    def c(self, value):
        """
        Set the length of the third side of the triangle. Must be positive.
        
        Parameters:
        - value: New length of the third side. Must be positive.
        
        Raises:
        - ValueError: If the length is not positive or if the sides do not form a triangle.
        """
        if value <= 0:
            raise ValueError("Side length must be positive.")
        self._c = value
        self._validate_triangle()

    def _validate_triangle(self):
        """
        Validate the sides to ensure they form a valid triangle.
        
        Raises:
        - ValueError: If the sides do not satisfy the triangle inequality theorem.
        """
        if not (self.a and self.b and self.c):
            return
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise ValueError("The given sides do not form a triangle.")

    @property
    def area(self):
        """
        Calculate the area of the triangle using Heron's formula.
        
        Returns:
        - The area of the triangle.
        """
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @property
    def perimeter(self):
        """
        Calculate the perimeter of the triangle.
        
        Returns:
        - The perimeter of the triangle.
        """
        return self.a + self.b + self.c

    def is_right_angle(self):
        """
        Check if the triangle is a right-angled triangle.
        
        Returns:
        - True if the triangle is right-angled, False otherwise.
        """
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)

    def __repr__(self):
        """
        Return a string representation of the triangle.
        
        Returns:
        - A string describing the triangle.
        """
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"

    def __eq__(self, other):
        """
        Check if this triangle is equal to another triangle.
        
        Parameters:
        - other: Another triangle to compare with.
        
        Returns:
        - True if the triangles have the same side lengths, False otherwise.
        """
        return isinstance(other, Triangle) and (self.a, self.b, self.c) == (other.a, other.b, other.c)

    def __lt__(self, other):
        """
        Compare this triangle with another triangle by area.
        
        Parameters:
        - other: Another triangle to compare with.
        
        Returns:
        - True if this triangle has a smaller area than the other triangle, False otherwise.
        """
        if isinstance(other, Triangle):
            return self.area < other.area
        return NotImplemented
