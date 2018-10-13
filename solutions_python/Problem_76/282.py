fi = open("input.txt")
T = int(fi.readline())
for test in range(T):
    n = int(fi.readline())
    a = map(int,fi.readline().split())
    a.sort()
    assert n == len(a)
    #print a
    s = 0
    for x in a:
        s = s^x
    res = "NO"
    if s==0:
        a.pop(0)
        res = sum(a)
    print "Case #{0}: {1}".format(test+1,res)
    
fi.close()