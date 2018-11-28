from itertools import groupby

class Quaternion(object):
    TABLE = {
        '1': {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'},
        'i': {'1': 'i', 'i': '1', 'j': 'k', 'k': 'j'},
        'j': {'1': 'j', 'i': 'k', 'j': '1', 'k': 'i'},
        'k': {'1': 'k', 'i': 'j', 'j': 'i', 'k': '1'},
    }

    SIGN = {
        '1': {'1': False, 'i': False, 'j': False, 'k': False},
        'i': {'1': False, 'i': True,  'j': False, 'k': True },
        'j': {'1': False, 'i': True,  'j': True,  'k': False},
        'k': {'1': False, 'i': False, 'j': True,  'k': True },
    }

    def __init__(self, v='1', n=False):
        self.val = v
        self.neg = n

    def __mul__(self, other):
        v = self.TABLE[self.val][other]
        n = self.neg ^ self.SIGN[self.val][other]
        return Quaternion(v, n)

    def __rmul__(self, other):
        v = self.TABLE[other][self.val]
        n = self.neg ^ self.SIGN[other][self.val]
        return Quaternion(v, n)

    def __repr__(self):
        return "Quaternion({}, {})".format(self.val, self.neg)

    def __str__(self):
        return ("-" if self.neg else "") + self.val

    def __eq__(self, other):
        return str(self) == other


def simplify(string):
    new_string = ""
    for k, g in groupby(string):
        new_string += k * (len(list(g)) % 10)
    return new_string


def check_partitions(data):
    # Find all prefixes that mul to i
    p_i = []
    q = Quaternion()
    for i, c in enumerate(data):
        q = q * c
        if q == "i":
            p_i.append(i+1)

    # find all postfixes that mul to k
    p_k = []
    q = Quaternion()
    for c in reversed(data):
        i -= 1
        q = c * q
        if q == "k":
            p_k.append(i+1)

    # Starting at each prefix that mul to i
    # keep muling until we get j and check if
    # the rest is a k postfix
    for i in p_i:
        j = i
        q = Quaternion()
        p_k = set(p_k)
        for c in data[i:]:
            j += 1
            q = q * c
            if q == "j" and j in p_k:
                return True
    return False

def check(data):
    q = Quaternion()
    for c in data:
        q *= c
    return q


T = int(raw_input())

for case in range(T):
    L, X = map(int, raw_input().split())
    # data = simplify(simplify(raw_input()) * X)
    data = raw_input() * X

    if check_partitions(data):
        print "Case #{}: YES".format(case + 1)
    else:
        print "Case #{}: NO".format(case + 1)
