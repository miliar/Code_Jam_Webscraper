import sys
number = int(sys.stdin.readline().rstrip('\n'))

for i in range(number):
    l = sys.stdin.readline().rstrip('\n').split(' ')
    r = int(l[0])
    k = int(l[1])
    n = int(l[2])
    l = sys.stdin.readline().rstrip('\n').split(' ')
    t = []
    for item in l:
        t.append(int(item))
    cash = 0
    for j in range(r):
        kk = k
        nn = n
        while (kk > 0 and nn > 0 and t[0] <= kk):
            kk -= t[0]
            nn -= 1
            cash += t[0]
            t.append(t.pop(0))
    print "Case #" + str(i+1) + ": " + str(cash)

