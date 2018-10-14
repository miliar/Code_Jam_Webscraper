# Google Code Jam 2015
# Qualification Round
# Problem A

t = int(raw_input())

for case in xrange(1,t+1):
    s,a = raw_input().split()
    c = 0
    x = 0
    for i in xrange(len(a)):
        if x < i:
            c += i-x 
            x = i
        x += ord(a[i]) - ord('0')
    print 'Case #%d: %d' % (case, c)
