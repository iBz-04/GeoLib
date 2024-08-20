![Logo](https://res.cloudinary.com/diekemzs9/image/upload/v1724152061/Geolib_logo_nelg32.jpg)


# GeoLib
This library is a new Python-based geometry package designed to facilitate easy manipulation of shapes. The initial version of the library primarily focuses on two fundamental shapes: Squares and Triangles. The project aims to be both educational and practical, making it useful for developers, students.

GeoLib is open-source under the MIT License, allowing developers to freely use, modify, and contribute to its ongoing development.

## Features

- Initialization with Side Length: Easily create a shape by specifying its side length.

- Area Calculation: Compute the area of the square using the area property.

- Perimeter Calculation: Compute the perimeter of the square using the perimeter property.

- Scaling: Scale the square by a given factor using the scale method, which allows for dynamic resizing of the square.

- Comparison Operators: Compare two squares using equality (==) and less than (<) operators based on their side lengths.

- Property Validation: Ensure that side lengths are positive, with robust error handling to prevent invalid geometric states.

- String Representation: Convenient string representation of the square, making it easy to display in output and debugging.

- The library is designed to be extensible, allowing developers to easily add support for additional geometric shapes beyond squares and triangles.


## Installation

Install the library with :

```bash
 pip install git+https://github.com/iBz-04/GeoLib.git
```
    
## Usage

```python
from geolib import Square

# Create a square with a side length of 4
square = Square(4)

# Calculate area and perimeter
print("Area:", square.area)           # Output: Area: 16
print("Perimeter:", square.perimeter) # Output: Perimeter: 16

# Scale the square by a factor of 2
square.scale(2)
print("New side length:", square.side_length)  # Output: New side length: 8

# Compare squares
small_square = Square(3)
print(square > small_square)  # Output: True

```


## License

GeoLib is licensed under the [MIT](https://github.com/iBz-04/GeoLib?tab=MIT-1-ov-file#readme) License.



##  Creators

- [@Ibrahim](https://github.com/iBz-04)
- [@Arda](https://github.com/cyrekWei)
