def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())
def readlinelist(foo): return list(readlinearray(foo))

import sys

MAX=10**19

def xcombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xcombinations(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc

def xuniqueCombinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in xuniqueCombinations(items[i+1:],n-1):
                yield [items[i]]+cc
            
def xselections(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for ss in xselections(items, n-1):
                yield [items[i]]+ss

def xpermutations(items):
    return xcombinations(items, len(items))

def hash_list(items):
    prime = 31
    result = 1
    for item in items:
        result = prime * result + item;
    return result

def xuniquePermutations(items):
    sofar = set()
    for p in xpermutations(items):
        h = hash_list(p)
        if h not in sofar:
            sofar.add(h)
            yield  p


def remap(number, p):
    r = ''
    for d in number:
        r += str(p.index(d))
    
    return r

assert remap('abc', ['a', 'b', 'c']) == '012'
assert remap('abca', ['a', 'b', 'c']) == '0120'
assert remap('cba', ['a', 'b', 'c']) == '210'

def get_base10_number_at_base(n, base):
    n = list(reversed(n))
    r = 0
    pow = 0
    for i in xrange(len(n)):
        r += n[i] * base ** pow
        pow += 1
    
    return r

def get_ans(number):
    
    map = {}
    t = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    index = 0
    nn = []
    base = max(2, len(list(set(list(number)))))
    for d in number:
#        if index >= len(t):
#            print 'Error!'
#            sys.exit(1)
        if not map.has_key(d):
            map[d] = t[index]
            index += 1
        nn.append(map.get(d))
    return get_base10_number_at_base(nn, base)
    

T = readint()


for case in xrange(1, T+1):
    
    number = raw_input()
    ans = get_ans(number)
    print 'Case #%d: %d' % (case, ans)