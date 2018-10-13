from re import *
from sys import stderr
import itertools
def readint():
    return int(raw_input())
def readfloat():
    return float(raw_input())
def readarray(N, foo=raw_input):
    return [foo() for i in xrange(N)]
def readlinearray(foo=int):
    return map(foo, raw_input().split())

def NOD(a, b):
    while b:
        a,b = b, a%b
    return a

def gen_primes(max):
    primes = [1]*(max+1)
    for i in range(2, max+1):
        if primes[i]:
            for j in range(i+i, max+1, i):
                primes[j] = 0
    primes[0] = 0
    return [x for x in range(max+1) if primes[x]]

def is_prime(N):
    i = 3
    if not(N % 2):
        return 0
    while i*i < N:
        if not(N % i):
            return 0
        i += 3
    return 1

def trie_size(s):
    nodes = set(itertools.chain(*[[ss[:i] for i in range(len(ss)+1)] for ss in s]))
    return len(nodes)

def gen(n, m, r = []):
    if m == 0:
        return [r]
    rr = []
    for i in range(n):
        rr += gen(n, m - 1, r + [i])
    return rr

def correct(x):
    max_was = -1
    for i in x:
        if i > max_was + 1:
            return False
        max_was = max(max_was, i)
    return True

def splits(s, n):
    r = []
    for c in gen(n, len(s)):
        cr = [[] for i in range(n)]
        for i in range(len(s)):
            cr[c[i]].append(s[i])
        r.append(cr)
    return r

case_number = readint()
for case in xrange(case_number):
    stderr.write('%d\n' % (case, ))
    M, N = readlinearray()
    s = [raw_input() for i in range(M)]
    cbest = -1
    cvar = 0
    for sp in splits(s, N):
        res = sum(map(trie_size, sp))
        if res > cbest:
            cbest = res
            cvar = 1
        elif res == cbest:
            cvar += 1
    print "Case #%s: %d %d" % (case + 1, cbest, cvar)
