# -*- coding: utf-8 -*-

__all__ = ["AddableTuple", "cacheDecorator"]

class AddableTuple(tuple):
    def __add__(self, y):
        if isinstance(y, AddableTuple):
            result = list()
        
            if(len(self) != len(y)):
                raise ValueError("Tuples must have the same qty of items.")
        
            for i in range(0, len(y)):
                result.append(self[i] + y[i])
        
            return self.__class__(result)
        else:
            return tuple.__add__(self, y)

def cacheDecorator(function):
    cache = dict()
    def cachedResult(*args, **kwargs):
        if not args in cache:
            cache[args] = function(*args, **kwargs)
        return cache[args]
    return cachedResult