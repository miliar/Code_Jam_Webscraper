#!/usr/bin/env python

TYP_OR = 0
TYP_AND = 1

class Node(object):
    def __init__(self, typ, changeable):
        self.typ = typ
        self.changeable = changeable
        self.val = None
    def __str__(self):
        return "%s %s %s" % ("AND" if self.typ else "OR ", "y" if
                self.changeable else "n", self.val)

def val(n):
    if not isinstance(n, Node):
        return n
    if n.typ == TYP_OR:
        n.val = val(n.a) | val(n.b)
    else:
        n.val = val(n.a) & val(n.b)
    return n.val

def x(n, to):
    if not isinstance(n, Node):
        return 0 if to == n else None
    if n.val == to:
        return 0
    if n.typ == TYP_OR:
        if to == 1:
            a = x(n.a, 1)
            b = x(n.b, 1)
            if a is None and b is None:
                return None
            elif a is None:
                return b
            elif b is None:
                return a
            else:
                return min(a, b)
        else: # to == 0
            a = x(n.a, 0)
            b = x(n.b, 0)
            if n.changeable:
                if a is None and b is None:
                    return None
                elif a is None:
                    return 1 + b
                elif b is None:
                    return 1 + a
                else:
                    return 1 + min(a, b)
            else: # not changeable
                if a is None or b is None:
                    return None
                else:
                    return a + b
    else: # n.typ == TYP_AND
        if to == 0:
            a = x(n.a, 0)
            b = x(n.b, 0)
            if a is None and b is None:
                return None
            elif a is None:
                return b
            elif b is None:
                return a
            else:
                return min(a, b)
        else: # to == 1
            a = x(n.a, 1)
            b = x(n.b, 1)
            if n.changeable:
                if a is None and b is None:
                    return None
                elif a is None:
                    return 1 + b
                elif b is None:
                    return 1 + a
                else:
                    return 1 + min(a, b)
            else:
                if a is None or b is None:
                    return None
                else:
                    return a + b

def gcj1():
    n, r = (int(e.strip()) for e in raw_input().split())
    nodes = []
    for i in xrange((n - 1) / 2):
        G, C = (int(e.strip()) for e in raw_input().split())
        nodes.append(Node(G, C))
    for i in xrange((n + 1) / 2):
        nodes.append(input())
    assert(len(nodes) == n)
    for i in xrange(2, n + 1, 2):
        nodes[i/2 - 1].a = nodes[i-1]
        nodes[i/2 - 1].b = nodes[i]
    val(nodes[0])
    num = x(nodes[0], r)
    print "IMPOSSIBLE" if num is None else num

def main():
    N = input()
    for i in xrange(1, N + 1):
        print "Case #%d:" % i,
        gcj1()

if __name__ == "__main__":
    main()
