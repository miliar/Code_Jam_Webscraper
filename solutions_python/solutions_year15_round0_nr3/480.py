import sys,os
import operator
from functools import reduce, partial
##debug = partial(print, file=sys.stderr)
#debug = lambda *a,**kw: None

BASES=list('1ijk')
# from wiki
mul_table = '''
×	1	i	j	k
1	1	i	j	k
i	i	−1	k	−j
j	j	−k	−1	i
k	k	j	−i	−1
'''

class QB:
    def __init__(self, base, val=1):
        if isinstance(base, str):
            s=base
            if s.startswith('-'):
                s = s.strip('-')
                self.val = -1
            else:
                self.val = 1
            self.base = BASES.index(s)
            self.val *= val
        else:
            assert base in range(len(BASES)) and val in {-1,1}
            self.base = base
            self.val = val

    def __mul__(self, other):
        r = QB(mul_table[self.base][other.base], self.val*other.val)
        return r

    def __eq__(self, other):
        return self.base == other.base and self.val == other.val

    def __pow__(self, p):
        r = QB('1')
        curpow = self
        while p:
            if p&1: r *= curpow
            curpow *= curpow
            p//=2
        return r

    def __repr__(self):
        return str(self.val).strip('1') + BASES[self.base]

mul_table = mul_table.strip().replace('−', '-')
mul_table = [ line.strip().split()[1:] for line in mul_table.split('\n')[1:] ]


def solve():
    L, X = map(int, input().split())
    s = input()
    assert len(s) == L
    iterprod = reduce(operator.mul, map(QB, s))
    totalprod = iterprod ** X
    #if L*X < 100:
        #debug("prefixes: ", ' '.join(str(reduce(operator.mul, map(QB, (s*X)[:pref]))) for pref in
        #range(1,1+L*X)))
    #debug("iterprod = %s, totalprod = %s"%(iterprod, totalprod))
    if totalprod != QB('-1'): return False # ijk = k^2 = -1
    def find(val, after = -1):
        # Find a prefix with product `val`
        prefprod = QB('1')
        for i in range(L):
            #debug("i =", i)
            prefprod *= QB(s[i])
            period_mult = QB('1')
            for repeat in range(min(8, X)): # 2 periods
                pos = L*repeat + i
                tmp = period_mult * prefprod
                #debug("POS %d VAL %s"%(pos, tmp))
                if tmp == val and pos > after: return pos
                period_mult *= iterprod
        return None
    pos1 = find(QB('i'))
    if pos1 is None: pos2=None
    else: pos2 = find(QB('k'), pos1) # k = ij
    #debug("i: %s, j: %s"%(pos1, pos2))
    return (pos1 is not None and pos2 is not None and pos2 > pos1)

if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T+1):
        print("Case",tc,file=sys.stderr)
        print("Case #%d: %s"%(tc, ['NO', 'YES'][bool(solve())]))

