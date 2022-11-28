# Singleton Pattern Implementation

## Overview

This repository contains an implementation of the Singleton design pattern in Python. This implementation includes a metaclass-based approach for enforcing the Singleton behavior and a decorator class for converting regular classes into singletons.

## Singleton Implementation

### MetaSingleton Metaclass

The `MetaSingleton` metaclass ensures that only one instance of any class using this metaclass is created. It maintains a dictionary of instances, where each key is the class representation (either `repr(cls)` if defined, or a combination of module and class name) and each value is the single instance of that class.

### Singleton Class

The `Singleton` class uses `MetaSingleton` as its metaclass. Any class inheriting from `Singleton` will automatically follow the singleton behavior.

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