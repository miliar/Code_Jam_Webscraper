n = int(raw_input())

def output1(k, st):
    stand = 0
    sum = 0
    for i in xrange(k+1):
        if i > stand and int(st[i])!=0:
            stand += i-stand
        stand += int(st[i])
        sum += int(st[i])
    return stand-sum

for i in xrange(n):
    ni, s = raw_input().strip().split()
    ans1= output1(int(ni), s)

    print 'Case #%d: %d' % (i+1, ans1)
