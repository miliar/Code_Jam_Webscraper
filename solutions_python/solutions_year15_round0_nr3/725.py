class Quaternion(object):
    def __init__(self, val, neg=False):
        self.val = val
        self.neg = neg

    def __mul__(self, b):
        multiplication = {
            '1': {'1': Quaternion('1'),
                'i': Quaternion('i'),
                'j': Quaternion('j'),
                'k': Quaternion('k')},
            'i': {'1': Quaternion('i'),
                'i': -Quaternion('1'),
                'j': Quaternion('k'),
                'k': -Quaternion('j')},
            'j': {'1': Quaternion('j'),
                'i': -Quaternion('k'),
                'j': -Quaternion('1'),
                'k': Quaternion('i')},
            'k': {'1': Quaternion('k'),
                'i': Quaternion('j'),
                'j': -Quaternion('i'),
                'k': -Quaternion('1')}
        }
        abs_res = multiplication[self.val][b.val]
        return abs_res if self.neg == b.neg else -abs_res

    def __eq__(self, b):
        return self.val == b.val and self.neg == b.neg

    def __ne__(self, b):
        return self.val != b.val or self.neg != b.neg

    def __neg__(self):
        return Quaternion(self.val, not self.neg)

    def __str__(self):
        return "{}{}".format('-' if self.neg else '', self.val)

def read(f):
    L, X = [int(n) for n in f.readline().split()]
    chars = [Quaternion(n) for n in f.readline()[:-1]]
    return L, X, chars

def calc(data):
    L, X, chars = data
    full = X*chars
    I, J, K = Quaternion('i'), Quaternion('j'), Quaternion('k')
    L_mult = Quaternion('1')
    for l in chars:
        L_mult = L_mult * l
    T_mult = Quaternion('1')
    for x in xrange(X):
        T_mult = T_mult * L_mult
    if T_mult != Quaternion('1', True):
        return False
    look_for_i = Quaternion('1')
    for i in xrange(L*X):
        look_for_i = look_for_i * full[i]
        if look_for_i == I:
            look_for_j = Quaternion('1')
            for j in xrange(i+1, L*X):
                look_for_j = look_for_j * full[j]
                if look_for_j == J:
                    look_for_k = Quaternion('1')
                    for k in xrange(j+1, L*X):
                        look_for_k = look_for_k * full[k]
                    if look_for_k == K:
                        return True
    return False

def write(solution):
    return 'YES' if solution else 'NO'

def solve(f):
    data = read(f)
    solution = calc(data)
    return write(solution)

if __name__ == '__main__':
    import sys
    with open(sys.argv[1]) as f:
        T = int(f.readline())
        for t in range(1, T+1):
            print('Case #{t}: {solution}'.format(t=t, solution=solve(f)))
