import sys
#import itertools
f = open(sys.argv[1])
T = int(f.readline())
for i in range(T):
    print "Case #" + str(i + 1) + ":",
    (N, P) = f.readline().split()
    N = int(N)
    P = int(P)
    n = 2 ** N
    #mn = [0] * n
    #mx = [0] * n

    i = 0   
    v = n / 2
    r = 2
    s = n / 4
    while s > 0 and v < P:
        i = i + r
        v = v + s
        s = s / 2
        r = r * 2
    
    if s == 0 and v < P:
        i = i + 1
    print i,

    i = 0
    v = 1
    r = n /2
    while r > 0 and v < P:
        i = i + r
        v = 2 * v + 1
        r = r / 2
    print i

    #i = 0
    #while i < len(mx) and mx[i] < P:
    #    i = i + 1
    #print i - 1,
    #i = 0
    #while i < len(mn) and  mn[i] < P:
    #    i = i + 1
    #print i - 1


#N = 3
#n = 2 ** N
#
#def solve(l):
#    global N
#    global n
#    table = []
#
#    for i in l:
#        table.append({"v":i, "r" : 0})
#
#    #print table
#    for i in range(N):
#        for g in range(n / 2):
#            if table[2*g]["v"] < table[2*g + 1]["v"]:
#                table[2*g]["r"]     = table[2*g]["r"] * 2
#                table[2*g + 1]["r"] = table[2*g + 1]["r"] * 2 + 1
#            else:
#                table[2*g]["r"]     = table[2*g]["r"] * 2 + 1
#                table[2*g + 1]["r"] = table[2*g + 1]["r"] * 2
#        table = sorted(table, key=lambda t : t["r"])
#        #print (table)
#
#    return [t["v"] for t in table]
#
#L = [i for i in range(n)]
#mn = list(L)
#mx=  list(L)
#
##print(solve([2,4,5,3,6,7,1,0]))
#
#for l in itertools.permutations(L):
#    res = solve(l)
#    for i in range(n):
#        if i < mn[res[i]]:
#            mn[res[i]] = i
#        if i > mx[res[i]]:
#            mx[res[i]] = i
#    print(mn, mx)
#    #break