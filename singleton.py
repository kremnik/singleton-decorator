class MetaSingleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if hasattr(cls, "__repr__"):
            repr_class_name = repr(cls)
        else:
            repr_class_name = cls.__module__ + "_" + cls.__name__
        if repr_class_name not in cls.__instances:
            cls.__instances[repr_class_name] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[repr_class_name]


class Singleton(metaclass=MetaSingleton):
    def __init__(self):
        pass


class singleton:
    def __new__(cls, *args, **kwargs):
        if len(args) < 1:
            raise ValueError("Cannot create a singleton without class.")
        class_ref = args[0]
        if not isinstance(class_ref, type):
            raise TypeError(f"Cannot create a singleton from {class_ref} because it is not a class.")
        if type(class_ref) != type:
            raise TypeError(f"Cannot create a singleton from {class_ref.__name__} because it already has a metaclass ({type(class_ref)}).")        
        if Singleton in class_ref.mro():
            return class_ref
        class_ref_properties = {name: getattr(class_ref, name) for name in dir(class_ref)}
        class_ref_properties["is_singleton"] = True
        return type(class_ref.__name__, (Singleton, ) + class_ref.__bases__, class_ref_properties)