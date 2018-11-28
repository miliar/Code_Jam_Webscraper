import sys

sys.stdin = open('A.in')

t = int(raw_input())

for i in xrange(t):
    s, k = raw_input().split()
    s = list(s)
    #print s
    k = int(k)
    ans = 0
    flag = True
    for j in xrange(len(s)):
        if s[j] == '-':
            if len(s) - j < k:
                flag = False
                break
            ans += 1
            try:
                for p in xrange(j, j+k):
                    if s[p] == '-':
                        s[p] = '+'
                    else:
                        s[p] = '-'
            except:
                pass
                    
    if flag:
        print 'Case #%d: %d' %(i+1, ans)
    else:
        print 'Case #%d: IMPOSSIBLE' %(i+1)
            
                