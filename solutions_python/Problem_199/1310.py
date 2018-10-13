import sys
sys.stdin  = open('input.in', 'r')
sys.stdout = open('output.txt', 'w')

for _ in xrange(1,input()+1):
    print 'Case #' + str(_) + ':',
    a, k = map(str,raw_input().split())
    s = []
    for i in a:
        s.append(i)
    k = int(k)
    l = len(s)
    ans = 0
    for i in xrange(l):
        if s[i] == '-':
            j = i
            f = 0
            while j < i + k and i + k <= l:
                if s[j] == '-' : s[j] = '+'
                else: s[j] = '-'
                j += 1
                f = 1
            if f : ans += 1
    for i in xrange(l):
        if s[i] == '-':
            ans = 'IMPOSSIBLE'
            break
    print ans