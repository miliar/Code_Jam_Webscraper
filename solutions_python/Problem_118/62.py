'''
Problem C. Fair and Square
Solution by vassnlit@gmail.com
'''

# found out the principle of building fair roots for "fair and square" numbers

# so precompute candidates for them first

'''
for l in xrange(2, 52 + 1):
    if l % 2 == 0:
        #GOOD.append(int('2%s2' % ('0' * (l-2))))
        print '2%s2' % ('0' * (l-2))
        L = (l-2)/2
        if L == 0:
            continue
        for n in xrange(2**L):
            s1 = ('0'*L + bin(n)[2:])[-L:]
            #GOOD.append(int('1%s%s1' % (s1, s1[::-1])))
            print '1%s%s1' % (s1, s1[::-1])
    else:
        #GOOD.append(int('2%s2' % ('0' * (l-2))))
        print '2%s2' % ('0' * (l-2))
        #GOOD.append(int('2%s1%s2' % ('0' * (l/2-1), '0' * (l/2-1))))
        print '2%s1%s2' % ('0' * (l/2-1), '0' * (l/2-1))
        L = (l-2)/2
        if L == 0:
            continue
        for j in (0, 1, 2):
            for n in xrange(2**L):
                s1 = ('0'*L + bin(n)[2:])[-L:]
                #GOOD.append(int('1%s%d%s1' % (s1, j, s1[::-1])))
                print '1%s%d%s1' % (s1, j, s1[::-1])
    #print l
'''

# then sort out bad ones
'''
GOOD = [0, 1, 2, 3, 11, 101, 111, 121]
def isGood(n):
    ns = str(n ** 2)
    return ns == ns[::-1]

for i in GOOD:
    print i
with open('tmp2','r') as inp:
    for l in inp:
        if isGood(int(l.strip())):
            print l.strip()
'''

# then use the data gathered for solving
with open('tmp3', 'r') as inp:
    nums = [(int(l.strip())**2) for l in inp]
ALL_FAIRS = sorted(set(nums))

def solve(a, b):
    for p, v in enumerate(ALL_FAIRS):
        if v >= a:
            break
    else:
        raise ValueError('no such square a')

    for q, v in enumerate(reversed(ALL_FAIRS)):
        if v <= b:
            break
    else:
        raise ValueError('no such square b')

    return len(ALL_FAIRS) - q - p

import sys
with open(sys.argv[1], 'r') as inp:
    T = int(inp.readline().strip())
    for t in xrange(T):
        A, B = [int(x) for x in inp.readline().strip().split()]
        print 'Case #%d: %d' % (t+1, solve(A, B))
