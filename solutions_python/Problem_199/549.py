class RangeBit:
    def __init__(self, n):
        sz = 1
        while n >= sz:
            sz *= 2
        self.size = sz
        self.dataAdd = [0]*sz
        self.dataMul = [0]*sz

    def sum(self, i):
        assert i > 0
        add = 0
        mul = 0
        start = i
        while i > 0:
            add += self.dataAdd[i]
            mul += self.dataMul[i]
            i -= i & -i
        return mul * start + add

    def get(self, i):
        assert i > 0
        if i == 1:
            return self.sum(1);
        else:
            return self.sum(i) - self.sum(i - 1);

    def put(self, i, val):
        assert i > 0
        self.add(i, i, val)

    def add(self, left, right, by):
        assert 0 < left <= right
        self._add(left, by, -by * (left - 1))
        self._add(right, -by, by * right)

    def _add(self, i, mul, add):
        assert i > 0
        while i < self.size:
            self.dataAdd[i] += add
            self.dataMul[i] += mul
            i += i & -i

def solve(S, K):
    len_S = len(S)
    PancakeBit = RangeBit(len_S)
    for i in range(len_S):
        if S[i] == '+': 
            PancakeBit.put(i+1, 0)
        elif S[i] == '-': 
            PancakeBit.put(i+1, 1)
        else: 
            print("Error! Should not have anything other than + or -")

    res = 0
    rightmost = len_S - K + 2
    for i in range(1, rightmost):
        if PancakeBit.get(i) % 2 == 1:
            PancakeBit.add(i, i + K - 1, 1)
            res += 1


    for i in range(rightmost, len_S + 1):
        if PancakeBit.get(i) % 2 == 1:
            return 'IMPOSSIBLE'

    return str(res)

T = input()
for t in range(1, T + 1):
    S, K = raw_input().split()
    K = int(K)
    print 'Case #%d: %s'%(t, solve(S, K))

