import inspect
from pprint import pprint

def introspection_info(obj):
    info = {}
    info['type'] = type(obj)
    info['attributes'] = [element for element in dir(obj) if not callable(getattr(obj, element))],
    info['methods'] = [element for element in dir(obj) if callable(getattr(obj, element))],
    info['module'] = inspect.getmodule(obj)
    return info
number_info = introspection_info(42)
print(number_info)

