class ValidType:
    def __init__(self, type):
        self.type = type

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise ValueError(f"Invalid type for {self.name}. Expected {self.type.__name__} ")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)


class Int(ValidType):
    def __init__(self):
        super().__init__(int)


class Float(ValidType):
    def __init__(self):
        super().__init__(float)


class List(ValidType):
    def __init__(self):
        super().__init__(list)


class Person:
    name = str()
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()

    def __init__(self, name, age, height, tags, favorite_foods):
        if not isinstance(name, str):
            raise ValueError(f"Invalid type for name. Expected str "
                             f"but got {name.__class__.__name__}.")
        self.name = name
        self.age = age
        self.height = height
        self.tags = tags
        self.favorite_foods = favorite_foods


try:
    p1 = Person("Bob", 33, 1.75, ['clever', 'nice'], ['pizza', 'apple'])
    print(p1.name)
    print(p1.age)
    print(p1.height)
    print(p1.tags)
    print(p1.favorite_foods)


except ValueError as e:
    print(e)