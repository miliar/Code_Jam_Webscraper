T = int(raw_input())

def con(arr):
    a = []
    a.append(int(arr[0]))
    for i in range(1,len(arr)):
        a.append(int(arr[i]))
    return a

for x in xrange(1, T + 1):
    n = [ s for s in raw_input().split(" ")]
    n = n[0]

    cont = True
    while cont:
        found = True
        c = con(n)
        for i in range(1,len(c)):
            if c[i] < c[i-1]:
                found = False
        if found:
            cont = False
            print "Case #{}: {}".format(x, n)
        else:
            if int(n) > 0:
                n = str(int(n) - 1)
