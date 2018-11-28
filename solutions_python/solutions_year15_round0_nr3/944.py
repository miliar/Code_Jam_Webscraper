import operator

def print_result(i, result):
    print 'Case #%s: %s' % (i+1, result)

class simple_quotanion(object):
    def __init__(self, c):
        if type(c) == str:
            if c == 'i':
                self._state = (0, 1, 0, 0)
            elif c == 'j':
                self._state = (0, 0, 1, 0)
            elif c == 'k':
                self._state = (0, 0, 0, 1)
            elif c == '1':
                self._state = (1, 0, 0, 0)
        else:
            self._state = tuple(c)
    def __eq__(self, other):
        return self._state == other._state
    def __ne__(self, other):
        return not (self == other)
    def __mul__(self, other):
        u1, i1, j1, k1 = self._state
        u2, i2, j2, k2 = other._state
        return simple_quotanion(
            ( + u1*u2 - i1*i2 - j1*j2 - k1*k2,
              + u1*i2 + i1*u2 + j1*k2 - k1*j2,
              + u1*j2 - i1*k2 + j1*u2 + k1*i2,
              + u1*k2 + i1*j2 - j1*i2 + k1*u2 ))
    def __neg__(self):
        return simple_quotanion(map(lambda x:-x, self._state))
    
    def __repr__(self):          # assuming only one of them is non-zero
        if self._state[0] != 0:
            return str(self._state[0])
        if self._state[1] != 0:
            if self._state[1] > 0:
                return 'i'
            else:
                return '-i'
        if self._state[2] != 0:
            if self._state[2] > 0:
                return 'j'
            else:
                return '-j'
        if self._state[3] != 0:
            if self._state[3] > 0:
                return 'k'
            else:
                return '-k'

U, I, J, K = map(simple_quotanion, ['1', 'i', 'j', 'k'])

def all_same_character(string):
    tmp = string[0]
    result = False
    for c in string:
        if c != tmp: return False
    return True

def check(string, X):
    # check if too short
    if len(string)*X < 3:
        debug('too short')
        return False
    # check if impossible from multiplication law
    qs = map(simple_quotanion, string)
    product = reduce(operator.mul, [reduce(operator.mul, qs)]*X)
    if product != -U:
        debug('sum is', product)
        return False
    # check if only one type of symbol is used
    if all_same_character(string): return False
    
    return True

def debug(*args):
    # print ' '.join(map(str, args))
    pass

def search(string, X):
    qs = map(simple_quotanion, string)*X
    first = U
    for i in xrange(len(qs)):
        first = first * qs[i]
        debug('first,', i, first)
        if first == I:
            second = U
            for j in xrange(i+1, len(qs)):
                second = second * qs[j]
                debug('second,', j, second)
                if second == J:
                    return True
    return False

def main():
    T = input()
    for i in range(T):
        L, X = map(int, raw_input().split(' '))
        string = raw_input()
        if not check(string, X):
            print_result(i, 'NO')
        else:
            if search(string, X):
                print_result(i, 'YES')
            else:
                print_result(i, 'NO')

if __name__ == '__main__':
    main()
