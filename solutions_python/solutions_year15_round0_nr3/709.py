import sys
import functools


mult = { 
    '1' : { '1' : '1', 'i' : 'i', 'j' : 'j', 'k': 'k'},
    'i' : { '1' : 'i', 'i' : '-1', 'j' : 'k', 'k': '-j'},
    'j' : { '1' : 'j', 'i' : '-k', 'j' : '-1', 'k': 'i'},
    'k' : { '1' : 'k', 'i' : 'j', 'j' : '-i', 'k': '-1'}}

l_inv = {
    '1' : '1',
    'i' : '-i',
    'j' : '-j',
    'k' : '-k'}

def left_inv(a):
    sign = 1
    if a[0] == '-':
        sign = -sign
    res = l_inv[a[-1]]
    if res[0] == '-':
        sign = -sign
    if sign > 0:
        return res[-1]
    return '-' + res[-1]

def mul(a, b):
    sign = 1
    if a[0] == '-':
        sign = -sign
    if b[0] == '-':
        sign = -sign
    res = mult[a[-1]][b[-1]]
    if res[0] == '-':
        sign = -sign
    if sign > 0:
        return res[-1]
    return '-' + res[-1]

class Fast:
    def __init__(self, s):
        self.s_m = []
        self.s_i = ['1']
        self.I = []
        self.K = []
        tmp = '1'
        for index, c in enumerate(s):
            tmp = mul(tmp, c)
            self.s_m.append(tmp)
            self.s_i.append(left_inv(tmp))
            if tmp == 'i':
                self.I.append(index + 1)
        for index, c in enumerate(self.s_i[:-1]):
            if mul(c, tmp) == 'k':
                self.K.append(index)

    def mul(self, i, j):
        return mul(self.s_i[i], self.s_m[j])

def solve(s):
    f = Fast(s)
    for left in f.I:
        for right in f.K:
            if left < right:
            #print('left = {}, right = {}, {}, {}, {}'.format(left, right, f.mul(0, left - 1), f.mul(left, right - 1), f.mul(right, len(s) - 1)))
                if (f.mul(0, left - 1) == 'i'
                        and f.mul(left, right - 1) == 'j'
                        and f.mul(right, len(s) - 1) == 'k'):
                    return True
    return False

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(1, T + 1):
        L, X = map(int, sys.stdin.readline().strip().split())
        s = sys.stdin.readline().strip()
        s = s * X
        if solve(s):
            print("Case #{}: YES".format(t))
        else:
            print("Case #{}: NO".format(t))


main()
