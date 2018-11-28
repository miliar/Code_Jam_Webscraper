import sys
import copy
import bisect

f = open(sys.argv[1])
if len(sys.argv)==3:
    debug = sys.argv[2]
else:
    debug = False
T = int(f.readline())

output = open(sys.argv[0][:-3] + 'output', 'w')

def solvecase(case):
    N = int(f.readline())
    naomib = [float(x) for x in f.readline().split()]
    kenb = [float(x) for x in f.readline().split()]
    if N == 1:
        if naomib[0] > kenb[0]:
            return 1, 1
        else:
            return 0, 0
    naomib1 = copy.deepcopy(naomib)
    kenb1 = copy.deepcopy(kenb)
    naomib1.sort()
    kenb1.sort()

    if float(N) >1:
        naomib.sort()
        kenb.sort()
    naomiscore = 0
    kenscore = 0

    for nbrick in copy.copy(naomib):
        kenb.sort()
        naomib.sort()
        kenbrick = bisect.bisect(kenb, nbrick)
        if kenbrick < len(kenb):
            kenbrick = kenb[kenbrick]
            kenb.remove(kenbrick)
            naomib.remove(nbrick)
            kenb.sort()
            naomib.sort()
            kenscore += 1
        else:
            kenb.pop(0)
            naomib.remove(nbrick)
            kenb.sort()
            naomib.sort()
            naomiscore += 1

    naomiscore1 = 0
    kenscore1 = 0
    plandeceit = 0

    if N > 1:
        while len(naomib1) > 0:
            nbrick = naomib1[0]

            if nbrick < kenb1[0]:
                plandeceit += 1
                naomib1.remove(nbrick)
                kenb1.pop()
                naomib1.sort()
                kenb1.sort()
                kenscore1 += 1

            else:
                naomib1.remove(nbrick)
                kenb1.pop(0)
                naomib1.sort()
                kenb1.sort()
                naomiscore1 += 1

    return naomiscore1, naomiscore
for t in range(T):
    result = solvecase(t+1)
    output.write("Case #{0}: {1} {2}\n".format(t+1, result[0], result[1]))
# solvecase(3)