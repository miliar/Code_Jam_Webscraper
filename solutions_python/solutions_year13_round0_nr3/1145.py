
import math
import itertools

#foo = []
total = 0
iter_range = lambda start, stop: iter(itertools.count(start).next, stop)

def rev_concat(seed, side):
    sseed = '{}'.format(seed)
    sside = '{}'.format(side)
    return long(sside+sseed+sside[::-1])

def start_NxN(a):
    aa = '{}'.format(a)
    lena = len(aa)
    if lena % 2 == 1:
        up = long(aa[0:lena//2] or 1)
    else:
        up = long(10**(lena//2-1))
    return up

def start_NxxN(a):
    aa = '{}'.format(a)
    lena = len(aa)
    if lena % 2 == 0:
        up = long(aa[0:lena//2-1] or 1)
    else:
        up = long(10**(lena//2-1))
    return up or 1

def gen_palindrome(a, b):
    bb = '{}'.format(b)
    lenb = len(bb)

    # palindromes of type N x N
    res = -1
    seeds = []
    # generate seeds
    for i in range(0, 10):
        seeds.append(i)
        if i < a or i > b: continue
        treat_pal(i)
    # compose seeds
    for side in iter_range(start_NxN(a), 10**(lenb//2)):
        for seed in seeds:
            res = rev_concat(seed, side)
            if res < a: continue
            if res > b: break
            treat_pal(res)
        if res > b : break

    # palindromes of type N xx N
    res = -1
    seeds = []
    # generate seeds
    for i in range(1, 10):
        seed = int('{}{}'.format(i, i))
        seeds.append(seed)
        if seed < a or seed > b: continue
        treat_pal(seed)
    # compose seeds
    stop = 10**(lenb//2-1)
    if stop < 1: stop = 1
    for side in iter_range(start_NxxN(a), stop):
        for seed in seeds:
            res = rev_concat(seed, side)
            if res < a : continue
            if res > b : break
            treat_pal(res)
        if res > b : break
    return

def is_palindrome(n):
    s = '{}'.format(n)
    for i in range(0, len(s)//2+1):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def treat_pal(n):
    global total
    if is_palindrome(n**2):
        total += 1
        #foo.append(n)

def solve(A, B):
    global total
    a = long(math.ceil(math.sqrt(A)))
    b = long(math.floor(math.sqrt(B)))
    total = 0
    gen_palindrome(a, b)
    return total

def main():
    #global foo
    T = int(raw_input())
    for t in iter_range(0, T):
        #foo = []
        A, B = map(long, raw_input().split(' '))
        res = solve(A, B)
        print 'Case #{}: {}'.format(t+1, res)

main()
