from math import pi

def next_permutation(s):
    s = list(s)
    for i in reversed(xrange(len(s))):
        if s[i] > s[i-1]:
            break
    else:
        return []
    i -= 1
    for j in reversed(xrange(i + 1, len(s))):
        if s[j] > s[i]:
            break
    t = s[i]
    s[i] = s[j]
    s[j] = t
    s[i + 1:] = reversed(s[i + 1:])
    return ''.join(s)

def cost(c):
    ret = 0.0
    for i in xrange(len(c)):
        if i == 0:
            ret += pi * c[i][0] * c[i][0]
        else:
            ret += (pi * c[i][0] * c[i][0]) - (pi * c[i-1][0] * c[i-1][0])
        ret += 2 * pi * c[i][0] * c[i][1]
    return ret

def solve(c,s):
    # print '~',s
    ret = []
    for i in xrange(len(s)):
        if s[i] == '1':
            ret.append(c[i])
    ret.sort()
    return cost(ret)

T = input()
for _ in xrange(T):
    N,K = raw_input().split(' ')
    N = int(N)
    K = int(K)
    c = []
    for i in xrange(N):
        ri,hi = raw_input().split(' ')
        c.append((int(ri), int(hi)))
    mask = '0'*(N-K) + '1'*K
    original_mask = mask[::-1]
    ret = 0.0
    while True:
        ir = solve(c,mask)
        if ir > ret:
            ret = ir
        # print '-',mask
        if mask == original_mask:
            break
        mask = next_permutation(mask)
        # print '+',mask
    print "Case #%s: %s" % (_+1, ret)