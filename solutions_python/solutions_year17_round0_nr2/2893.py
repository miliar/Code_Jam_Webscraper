def is_tidy(n):
    len_n = len(str(n))
    for i in xrange(len_n - 1):  
        d1 = (n / (10 ** (len_n - 1 - i))) % 10
        d2 = (n / (10 ** (len_n - 2 - i))) % 10
        if  d1 > d2: 
            return False

    return True

def make_tidy(n):
    l = str(n)
    r = []
    for i in xrange(len(l) - 1):
        r.append(l[i])
        if l[i] > l[i + 1]: 
            r[-1] = str(int(r[-1]) - 1) 
            break

    for j in xrange(i + 1, len(l)):
        r.append('9')

    ans = int(''.join(r))
    if not is_tidy(ans):
        for i in xrange(len(r) - 1, 0, -1):
            if r[i - 1] > r[i]:
                r[i] = '9'
                r[i - 1] = str(int(r[i - 1]) - 1)

        ans = int(''.join(r))

    return ans

for c in xrange(1, int(raw_input()) + 1):
    n = int(raw_input())
    if is_tidy(n):
        ans = n
    else:
        ans = make_tidy(n)

    print "Case #%d: %s" % (c, ans)
