import re,sys

numCases = int(sys.stdin.readline())
cases = []


sys.setrecursionlimit(1000000000)

for n in range(numCases):
    cases.append(re.split(r'\s+',sys.stdin.readline().strip()))

def possible(d, g, pd, pg):
    if (d * pd) % 100 != 0:
        return False
    else:
        if (g * pg) % 100 == 0:
            return True
        elif g < 100000000:
            return possible(d, g + 1, pd, pg)
        else:
            return False


i = 1
for case in cases:
    N = int(case[0])
    Pd = int(case[1])
    Pg = int(case[2])

    D = 1
    result = False
    if Pg == 100 and Pd != 100:
        result = False
    elif Pg == 0 and Pd != 0:
        result = False
    else:
        while D < N + 1:
            result = possible(D,D,Pd,Pg)
            if result:
                D = N + 1
            else:
                D = D + 1
    
    if result:
        print "Case #" + str(i) + ": " + "Possible"
    else:
        print "Case #" + str(i) + ": " + "Broken"
    i = i + 1
