class Int:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be integer")
        elif self.min_value is not None and self.min_value > value:
            raise ValueError(f"{self.name} must at least {self.min_value}")
        elif self.max_value is not None and self.max_value < value:
            raise ValueError(f"{self.name} must not exceed {self.max_value}")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.name, None)


class Point2D:
    x = Int(min_value=0, max_value=25)
    y = Int(min_value=0, max_value=25)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point2D: (x={self.x}, y={self.y})"

    def __str__(self):
        return f"{self.x}, {self.y}"


class Point2DSequence:
    def __init__(self, sequence, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length
        if len(sequence) < self.min_length or len(sequence) > self.max_length:
            raise ValueError(f"The length of the sequence must be between {self.min_length} "
                             f"and {self.max_length}")
        self.sequence = sequence

    def __setitem__(self, instance, value):
        from collections.abc import Sequence
        if not isinstance(value, Sequence):
            raise TypeError("The seq must be sequence")
        if len(self.sequence) < self.min_length or len(self.sequence) > self.max_length:
            raise ValueError(f"The length of the sequence must be between {self.min_length} "
                             f"and {self.max_length}")
        for i in self.sequence:
            if not isinstance(i, Point2D):
                raise ValueError('All elements in the sequence must be Point2D.')
        self.sequence.append(value)

    def __getitem__(self, item):
        if item is None:
            return self
        else:
            return self.sequence[item]

    def __len__(self):
        return len(self.sequence)


class Polygon:

    def __init__(self, vertices):
        if not isinstance(vertices, Point2DSequence):
            raise ValueError("Vertices must be of a type Point2DSequence")
        self.vertices = vertices

    def append_vertices(self, point):
        if not isinstance(point, Point2D):
            raise ValueError(f"Invalid types for point expected Point2D but got {point.__class__.__name__}")
        if len(self.vertices.sequence) >= self.vertices.max_length:
            raise ValueError("The maximum number of vertices is already available")
        else:
            self.vertices.sequence.append(point)


try:
    pt1 = Point2D(5, 2)
    pt2 = Point2D(7, 8)
    vert = Point2DSequence([pt1, pt2], 0, 5)
    pol = Polygon(vert)
    print(pol.vertices.sequence)
    pt3 = Point2D(8, 5)
    pol.append_vertices(pt3)
    print(pol.vertices.sequence)
except ValueError as ve:
    print(str(ve))
except TypeError as te:
    print(str(te))
