#!/usr/bin/env python3
#coding: utf-8
import sys
import unittest
from io import StringIO
from collections import deque

class Quaternion(object):
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.elems = (w, x, y, z)

    def __iter__(self):
        for el in self.elems:
            yield  el

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            q = Quaternion(
                self.w*other.w - self.x*other.x - self.y*other.y - self.z*other.z,
                self.w*other.x + self.x*other.w + self.y*other.z - self.z*other.y,
                self.w*other.y - self.x*other.z + self.y*other.w + self.z*other.x,
                self.w*other.z + self.x*other.y - self.y*other.x + self.z*other.w
            )
        else:
            q = Quaternion(*[comp*other for comp in self])
        return q

    def __eq__(self, other):
        return self.elems == other.elems

    def __ne__(self, other):
        return not self == other

    def __neg__(self):
        return Quaternion(*[-comp for comp in self])

    def __repr__(self):
        if self == o:
            r = '1'
        elif self == -o:
            r = '-1'
        elif self == i:
            r = 'i'
        elif self == -i:
            r = '-i'
        elif self == j:
            r = 'j'
        elif self == -j:
            r = '-j'
        elif self == k:
            r = 'k'
        elif self == -k:
            r = '-k'
        else:
            r = '?'
        return r

i = Quaternion(0,1,0,0)
j = Quaternion(0,0,1,0)
k = Quaternion(0,0,0,1)
o = Quaternion(1,0,0,0)

table = {
    'i':i,
    'j':j,
    'k':k,
}


def folduntil(deq, until):
    result = False
    current = table[deq.popleft()]
    if current == until:
        return True
    while True:
        if len(deq) == 0:
            break
        pop = deq.popleft()
        new = current*table[pop]
        if new == until:
            result = True
            break
        if len(deq) == 0:
            break
        current = new
    return result


def fold(deq):
    current = table[deq.popleft()]
    if len(deq) == 0:
        return current
    while deq:
        pop = deq.popleft()
        current = current*table[pop]
    return current


def solve_case(line, len_, repeatcount):
    if len_*repeatcount < 3:
        return False
    deq = deque(line*repeatcount)
    if not folduntil(deq, i):
        return False
    if not folduntil(deq, j):
        return False
    if not folduntil(deq, k):
        return False
    if len(deq) == 0:
        return True
    else:
        if fold(deq) == o:
            return True
        else:
            return False


def solve(inp, outp):
    N = int(inp.readline().strip())
    for i in range(0, N):
        L, repeatcount = map(int, inp.readline().strip().split())
        line = inp.readline().strip()
        result = solve_case(line, L, repeatcount)
        outp.write('Case #%d: %s\n' % (i+1, 'YES' if result else 'NO'))
        outp.flush()


test_data = \
'''6
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i
7 1
ijkiijj
'''

test_result = \
'''Case #1: NO
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: NO
Case #6: YES
'''

class MagicTest(unittest.TestCase):
    def test_magic_usual(self):
        outp = StringIO()
        solve(StringIO(test_data), outp)
        self.assertEqual(outp.getvalue(), test_result)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        sys.argv.pop()
        unittest.main()
    else:
        solve(sys.stdin, sys.stdout)
