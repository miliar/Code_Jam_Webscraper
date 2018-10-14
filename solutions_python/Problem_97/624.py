#Paul Johnson
#GCJ 2012 Problem C


from sys import *

def remDup(l):
    res = [l[0]]
    for x in l:
        if res[-1] != x: res.append(x)
    return res

input = open(argv[1],'r')
output = open(argv[2],'w')

testCases = int(input.readline())

for x in range(testCases):
    if not x%5: print x
    l = input.readline().split()
    min = int(l[0])
    max = int(l[1])
    count = 0
    outl = []
    for y in range(min,max+1):
        y = str(y)
        ln = len(y)
        for z in range(1,ln):
            p = y[z:]+y[:z]
            if int(p) <= max and int(p) >= min and p[0] != 0 and y != p:
                pair = [y,p]
                pair.sort()
                outl.append(pair)

#                    print p

#    print outl
    outl.sort()
    if outl:
#        print remDup(outl)
        ans = len(remDup(outl))
    else: ans = 0
    output.write("Case #%i: %i\n"%(x+1, ans))

output.close()
input.close()