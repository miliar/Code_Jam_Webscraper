#!/usr/bin/env python3

quat = ['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k']
# a * b = c -> c = mul[a][b]
mul = [
        [0, 1, 2, 3, 4, 5, 6, 7],
        [1, 4, 3, 6, 5, 0, 7, 2],
        [2, 7, 4, 1, 6, 3, 0, 5],
        [3, 2, 5, 4, 7, 6, 1, 0],
        [4, 5, 6, 7, 0, 1, 2, 3],
        [5, 0, 7, 2, 1, 4, 3, 6],
        [6, 3, 0, 5, 2, 7, 4, 1],
        [7, 6, 1, 0, 3, 2, 5, 4]]
# a * b = c -> b = ldiv[c][a]
ldiv = [[0, 5, 6, 7, 4, 1, 2, 3],
        [1, 0, 3, 6, 5, 4, 7, 2],
        [2, 7, 0, 1, 6, 3, 4, 5],
        [3, 2, 5, 0, 7, 6, 1, 4],
        [4, 1, 2, 3, 0, 5, 6, 7],
        [5, 4, 7, 2, 1, 0, 3, 6],
        [6, 3, 4, 5, 2, 7, 0, 1],
        [7, 6, 1, 4, 3, 2, 5, 0]]
# a * b = c -> a = rdiv[c][b]
rdiv = [[0, 5, 6, 7, 4, 1, 2, 3],
        [1, 0, 7, 2, 5, 4, 3, 6],
        [2, 3, 0, 5, 6, 7, 4, 1],
        [3, 6, 1, 0, 7, 2, 5, 4],
        [4, 1, 2, 3, 0, 5, 6, 7],
        [5, 4, 3, 6, 1, 0, 7, 2],
        [6, 7, 4, 1, 2, 3, 0, 5],
        [7, 2, 5, 4, 3, 6, 1, 0]]
# a ** b = c -> c = power[a][b]
power = [
        [0, 0, 0, 0],
        [0, 1, 4, 5],
        [0, 2, 4, 6],
        [0, 3, 4, 7],
        [0, 4, 0, 4],
        [0, 5, 4, 1],
        [0, 6, 4, 2],
        [0, 7, 4, 3]]

class Quaternion:
    def __init__(self, s='1'):
        self.negative = False
        if s.startswith('-'):
            self.negative = True
            s = s[1:]
        elif s.startswith('+'):
            s = s[1:]

        if s not in ['1', 'i', 'j', 'k']:
            raise ValueError
        self.unit = s

    def __str__(self):
        if self.negative:
            return '-' + self.unit
        else:
            return self.unit

    __repr__ = __str__

    def __eq__(self, other):
        if isinstance(other, str):
            other = Quaternion(other)
        return self.negative == other.negative and self.unit == other.unit

    def __copy__(self):
        new = Quaternion()
        new.negative = self.negative
        new.unit = self.unit
        return new

    def __neg__(self):
        new = self.__copy__()
        new.negative = not new.negative
        return new

    def __imul__(self, other):
        if isinstance(other, str):
            other = Quaternion(other)

        otherNeg = other.negative

        if self.unit == '1':
            self.unit = other.unit
        elif other.unit == '1':
            pass
        elif self.unit == 'i':
            if other.unit == 'i':
                self.unit = '1'
                self.negative = not self.negative
            elif other.unit == 'j':
                self.unit = 'k'
            else:
                self.unit = 'j'
                self.negative = not self.negative
        elif self.unit == 'j':
            if other.unit == 'i':
                self.unit = 'k'
                self.negative = not self.negative
            elif other.unit == 'j':
                self.unit = '1'
                self.negative = not self.negative
            else:
                self.unit = 'i'
        else:
            if other.unit == 'i':
                self.unit = 'j'
            elif other.unit == 'j':
                self.unit = 'i'
                self.negative = not self.negative
            else:
                self.unit = '1'
                self.negative = not self.negative

        self.negative ^= otherNeg
        return self

    def __mul__(self, other):
        new = self.__copy__()
        new *= other
        return new

    def __itruediv__(self, other): # other * ? = self
        if isinstance(other, str):
            other = Quaternion(other)

        otherNeg = other.negative

        if other.unit == '1':
            pass
        elif self.unit == '1':
            self.unit = other.unit
            self.negative = not self.negative
        elif self.unit == other.unit:
            self.unit = '1'
        elif other.unit == 'i':
            if self.unit == 'j':
                self.unit = 'k'
                self.negative = not self.negative
            else:
                self.unit = 'j'
        elif other.unit == 'j':
            if self.unit == 'i':
                self.unit = 'k'
            else:
                self.unit = 'i'
                self.negative = not self.negative
        else:
            if self.unit == 'i':
                self.unit = 'j'
                self.negative = not self.negative
            else:
                self.unit = 'i'

        self.negative ^= otherNeg
        return self

    def __truediv__(self, other):
        new = self.__copy__()
        new /= other
        return new

    def __ipow__(self, other):
        other %= 4
        if other == 0:
            return Quaternion('1')
        other -= 1
        selfcopy = self.__copy__()
        for _ in range(other):
            self *= selfcopy
        return self

    def __pow__(self, other):
        new = self.__copy__()
        new **= other
        return new

    def rdiv(self, other): # ? * other = self
        self = self.__copy__()

        if other.unit == '1':
            pass
        elif self.unit == '1':
            self.unit = other.unit
            self.negative = not self.negative
        elif self.unit == other.unit:
            self.unit = '1'
        elif other.unit == 'i':
            if self.unit == 'j':
                self.unit = 'k'
            else:
                self.unit = 'j'
                self.negative = not self.negative
        elif other.unit == 'j':
            if self.unit == 'i':
                self.unit = 'k'
                self.negative = not self.negative
            else:
                self.unit = 'i'
        else:
            if self.unit == 'i':
                self.unit = 'j'
            else:
                self.unit = 'i'
                self.negative = not self.negative


        self.negative ^= other.negative
        return self


def getMul(fromStart, i, j):
    l = len(fromStart) - 1

    period = (j // l - i // l) % 4
    i = i % l
    j = j % l

    retval = power[fromStart[-1]][period]
    retval = mul[retval][fromStart[j]]
    retval = ldiv[retval][fromStart[i]]

    return retval

def solve(s, x):
    fromStart = [0]
    s = [1 if c == 'i' else 2 if c == 'j' else 3 for c in s]
    for c in s:
        fromStart.append(mul[fromStart[-1]][c])

    fromEnd = [fromStart[-1]]
    for c in s:
        fromEnd.append(ldiv[fromEnd[-1]][c])
    fromEnd.reverse()

    iPos = -1
    i = 1
    iPeriod = 0

    while True:
        try:
            iPos = fromStart.index(i, iPos+1)
        except ValueError:
            i = ldiv[i][fromStart[-1]]
            iPeriod += 1
            if i == 1:
                return False
            iPos = -1
            continue

        if iPeriod >= x:
            return False

        kPos = -1
        k = 3
        kPeriod = 0

        while True:
            try:
                kPos = fromEnd.index(k, kPos+1)
            except ValueError:
                k = rdiv[k][fromEnd[-1]]
                kPeriod += 1
                if k == 3:
                    break
                kPos = -1
                continue

            left = iPos + iPeriod * len(s)
            right = (x-kPeriod)*len(s) - kPos

            if left >= right:
                break

            if getMul(fromStart, left, right) == 2:
                return True


if __name__ == '__main__':
    import sys
    n = int(input())
    for i in range(1, n+1):
        print(i, file=sys.stderr)
        l, x = [int(s) for s in input().split()]
        s = input()
        print('Case #{0}:'.format(i), 'YES' if solve(s, x) else 'NO')
