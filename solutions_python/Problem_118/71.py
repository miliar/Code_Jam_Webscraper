from math import sqrt, ceil

def is_palyndrome(number):
    nStr = str(number)
    half = len(nStr) / 2
    for i in xrange(half):
        if nStr[i] != nStr[-1-i]:
            return False
    return True

def solve(A, B, roots):
    a = 0
    while roots[a]*roots[a] < A:
        a += 1
    b = len(roots)-1
    while roots[b]*roots[b] > B:
        b -= 1
    return b-a+1

def generate_fair_roots(upper_length):
    fair_roots = list()
    if upper_length >= 1:
        fair_roots += [1,2,3]
    if upper_length >= 2:
        fair_roots += [11,22]
    if upper_length >= 3:
        fair_roots += [101,111,121,202,212]
    for d in xrange(1, upper_length/2):
        for b in xrange(2**d):
            binstr = bin(b)[2:].rjust(d, '0')
            for center in ['','0','1','2']:
                for last_digit in ['1','2']:
                    half = binstr + last_digit
                    candidate = int(half[::-1] + center + half)
                    if is_palyndrome(candidate**2):
                        fair_roots.append(candidate)
    fair_roots.sort()
    return fair_roots

#roots = generate_fair_roots(50)
#for root in roots:
#    print root
roots = list()
f = open('roots.txt')
for line in f:
    roots.append(int(line))
f.close()

T = int(input())
for t in range(T):
    A,B = [int(s) for s in raw_input().split()]
    print 'Case #' + str(t+1) + ': ' + str(solve(A, B, roots))

