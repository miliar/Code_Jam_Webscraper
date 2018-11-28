from sys import stdin
cases = int(stdin.readline())
for i in range(1, cases + 1):
    lin = stdin.readline().split()
    d = int(lin[0])
    n = int(lin[1])
    ans = float('inf')
    for hors in range(n):
        lin = stdin.readline().split()
        k = d - int(lin[0])
        s = float(lin[1])
        ans = min(ans, s * d/ k)
    print "Case #"+str(i)+": "+"%.9f" % ans
