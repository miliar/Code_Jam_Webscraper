import sys
sys.stdin  = open('input.in', 'r')
sys.stdout = open('output.txt', 'w')

for _ in xrange(1,input()+1):
    print 'Case #' + str(_) + ':',
    n = raw_input()
    N = []
    for i in n:
        N.append(int(i))
    l = len(N)
    t = []
    while True:
        t, j = list(N), -1
        for i in xrange(l-1):
            if N[i+1] < N[i]:
                N[i] -= 1
                j = i+1
                break
        while 0 <= j < l:
            N[j] = 9
            j += 1
        f = 0
        for i in xrange(l):
            if N[i] != t[i]:
                f = 1
                break
        if f == 0:
            break
    ans = 0
    for i in xrange(l):
        ans = ans*10 + N[i]
    print ans
