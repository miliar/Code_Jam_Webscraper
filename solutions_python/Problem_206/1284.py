import sys

sys.stdin = open('A.in')

t = int(raw_input())

for i in xrange(t):
    des, n = map(int, raw_input().split())
    time = []
    for j in xrange(n):
        k ,s = map(int, raw_input().split())
        time.append(float(abs(des-k))/s)
    ans = 0
    try:
        ans = float(des)/max(time)
    except:
        ans = 10000
    print 'Case #%d: %0.8f' %(i+1, ans)