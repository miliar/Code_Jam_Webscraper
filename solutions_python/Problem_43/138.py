import sys

def parse_number(s):
    s = list(s)
    m = {}
    count = 1
    for i in xrange(len(s)):
        if s[i] in m:
            s[i] = m[s[i]]
        else:
            if len(m) == 1:
                m[s[i]] = 0
                s[i] = m[s[i]]
            else:
                m[s[i]] = count
                s[i] = m[s[i]]
                count += 1
    return s, count

def trans(s):
    n, c = parse_number(s)
    sum = 0
    for i in n:
        sum *= c
        sum += i
    return sum

if __name__ == '__main__':
    rl = sys.stdin.readline
    N = int(rl())
    for case in xrange(1, N+1):
        print 'Case #%d: %d' % (case, trans(rl().rstrip()))
