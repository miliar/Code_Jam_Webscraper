def mul(a, b, sign):
    if a == 'i':
        if b == 'i':
            return '1', sign * -1
        elif b == 'j':
            return 'k', sign
        elif b == 'k':
            return 'j', sign * -1
    elif a == 'j':
        if b == 'i':
            return 'k', sign * -1
        elif b == 'j':
            return '1', sign * -1
        elif b == 'k':
            return 'i', sign
    elif a == 'k':
        if b == 'i':
            return 'j', sign 
        elif b == 'j':
            return 'i', sign * -1
        elif b == 'k':
            return '1', sign * -1
    else:
        return b, sign

def solve():
    l, rep = map(int, raw_input().split())
    [s] = raw_input().split()

    if s == "k" * len(s) or s == "i" * len(s):
        return "NO"

    if len(s) % 2 == 0:
        if s == "ki" * (len(s) / 2):
            return "NO"
    ans = '1'
    sign = 1
    for i in s:
        ans, sign = mul(ans, i, sign)
    s_v, s_sign = ans, sign
#    print s_sign, s_v
   
    m = {1: [s_v, s_sign]}
    cnt = 2
    while cnt < rep:
#        print m[cnt/2]
        [s_v, s_sign] = m[cnt/2]
        m[cnt] = list(mul(s_v, s_v, s_sign * s_sign))
        cnt *= 2

    cnt = max(1, cnt/2)

    ans = '1'
    sign = 1
    [s_v, s_sign] = m[cnt]
    
    while rep:
        if rep >= cnt:
            rep -= cnt
            ans, sign = mul(ans, s_v, sign * s_sign)
        else:
            cnt /= 2
            [s_v, s_sign] = m[cnt]

#    for _ in xrange(rep):
#        ans, sign = mul(ans, s_v, sign * s_sign)
   
    if ans == '1' and sign == -1:
        return "YES"
    else:
        return "NO"

T = input()
for i in xrange(T):
    print 'Case #%d: %s' % (i + 1, solve())
