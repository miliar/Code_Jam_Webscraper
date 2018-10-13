import sys

n = int(sys.stdin.readline())
for i in xrange(1,n+1):
    case = sys.stdin.readline().strip()
    symbols = {}
    symbols[case[0]] = 1
    p=1
    while p<len(case) and case[p] == case[0]:
        p+=1

    if p<len(case):
        symbols[case[p]] = 0
    
    k=2
    for c in case[p:]:
        if c not in symbols:
            symbols[c] = k
            k+=1

    V = 0
    for c in xrange(len(case)):
        V += symbols[case[c]]*k**(len(case)-1-c)

    print "Case #" + str(i) + ":",V

