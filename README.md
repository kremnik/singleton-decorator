## Singleton Pattern Implementation

### MetaSingleton Metaclass

The `MetaSingleton` metaclass ensures that only one instance of any class using this metaclass is created. It maintains a dictionary of instances, where each key is the class representation (either `repr(cls)` if defined, or a combination of module and class name) and each value is the single instance of that class.

### Singleton Class

The `Singleton` class uses `MetaSingleton` as its metaclass. Any class inheriting from `Singleton` will automatically follow the singleton behavior.

### singleton Decorator Class

The `singleton` class is a decorator class. Its task is to add the `Singleton` class to the list of base classes of the decorated class. As a result, because the `Singleton`'s metaclass is `MetaSingleton`, the decorated class inherits this metaclass and becomes a singleton.

## Usage

```python
from singleton import singleton

@singleton
class RegularClass:
    def __init__(self):
        print("Initializing RegularClass")

    @classmethod
    def classname(cls):
        return cls.__name__

# The "singletoned" class is the original class (not a Singleton class, not a function, etc.)
print(RegularClass.classname() == "RegularClass") # Outputs: True

obj1 = RegularClass()
obj2 = RegularClass()

print(obj1 is obj2) # Outputs: True

# Check if class or instance is a singleton
print(hasattr(RegularClass, "is_singleton")) # Outputs: True
print(hasattr(obj1, "is_singleton")) # Outputs: True