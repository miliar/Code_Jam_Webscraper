def digit(c):
    return ord(c)-ord('0')

def work(x):
    for i in xrange(1, len(x)):
        if x[i] < x[i-1]:
            return work(str(int(x[:i])-1))+('9'*(len(x)-i))
    return x

tt = int(raw_input())
for t in xrange(1, tt+1):
    num = raw_input().strip()
    ans_raw = work(num)
    ans = str(int(ans_raw))
    print 'Case #%d: %s' % (t, ans)
