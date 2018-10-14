#!/usr/bin/env python3


from math import floor, ceil
from collections import OrderedDict, Callable


def main():
    t = int(input())

    for x in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        y, z = calcLastStallDistance(n, k)
        print("Case #{}: {} {}".format(x, y, z))


def calcLastStallDistance(numStalls, numUsers):
    ls = rs = None
    segments = DefaultOrderedDict(int, [(numStalls, 1)])

    while numUsers > 0:
        segmentSize, segmentCount = segments.popitem(last=False)
        numUsers -= segmentCount
        half = (segmentSize - 1) / 2
        ls = floor(half)
        rs = ceil(half)
        segments[rs] += segmentCount
        segments[ls] += segmentCount

    return [rs, ls]


class DefaultOrderedDict(OrderedDict):
    # Source: http://stackoverflow.com/a/6190500/562769
    def __init__(self, default_factory=None, *a, **kw):
        if (default_factory is not None and
           not isinstance(default_factory, Callable)):
            raise TypeError('first argument must be callable')
        OrderedDict.__init__(self, *a, **kw)
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return OrderedDict.__getitem__(self, key)
        except KeyError:
            return self.__missing__(key)

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = value = self.default_factory()
        return value

    def __reduce__(self):
        if self.default_factory is None:
            args = tuple()
        else:
            args = self.default_factory,
        return type(self), args, None, None, self.items()

    def copy(self):
        return self.__copy__()

    def __copy__(self):
        return type(self)(self.default_factory, self)

    def __deepcopy__(self, memo):
        import copy
        return type(self)(self.default_factory,
                          copy.deepcopy(self.items()))

    def __repr__(self):
        return 'OrderedDefaultDict(%s, %s)' % (self.default_factory,
                                               OrderedDict.__repr__(self))


main()
