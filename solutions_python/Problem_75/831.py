#!/usr/bin/env python

import sys


class Experiment(object):
    
    def __init__(self):
        self.list = []
        self.combined = dict()
        self.opposed = set()
    
    def add_combined(self, a, b, c):
        """a+b->c"""
        self.combined[(a, b)] = self.combined[(b, a)] = c
    
    def add_opposed(self, a, b):
        self.opposed.add((a, b))
        self.opposed.add((b, a))

    def tail(self):
        return tuple(self.list[-2:])

    def invoke(self, c):
        self.list.append(c)
        # combine all
        combined = False
        while len(self.list) >= 2:
            result = self.combined.get(self.tail())
            if result:
                self.list[-2:] = [result]
                combined = True
            else:
                break
        # opposing?
        if not combined:
            for item in self.list:
                if (item, c) in self.opposed:
                    self.list[:] = []
                    break

    def __str__(self):
        return '[%s]' % ', '.join(self.list)


def main(fp=sys.stdin):
    fp.readline()
    case = 1
    for line in fp:
        words = line.split()
        ex = Experiment()
        i = 1
        for _ in xrange(int(words[0])):
            ex.add_combined(*words[i])
            i += 1
        for _ in xrange(int(words[i])):
            i += 1
            ex.add_opposed(*words[i])
        for c in words[-1]:
            ex.invoke(c)
        print 'Case #%d: %s' % (case, ex)
        case += 1

if __name__ == '__main__':
    main()
