import sys

T = int(sys.stdin.readline())

def war(N, noami, ken):
    i = 0
    j = 0
    kenc = 0
    while (i<N and j<N):
        if (noami[i] > ken[j]):
            j = j + 1
            continue
        else:
            i = i + 1
            j = j + 1
            kenc = kenc + 1
            continue

    return N - kenc

def dwar(N, noami, ken):
    i = 0
    j = 0
    noamic = 0
    while (i<N and j<N):
        if (noami[i] > ken[j]):
            i = i + 1
            j = j + 1
            noamic = noamic + 1
            continue
        else:
            i = i + 1
            continue

    return noamic

for case in range(0,T):
    N = int(sys.stdin.readline())
    noami = map(float, sys.stdin.readline().split())
    ken   = map(float, sys.stdin.readline().split())
    noami.sort()
    ken.sort()
    
#     print noami
#     print ken
    
    print "Case #" + str(case+1) + ": " + str(dwar(N, noami, ken)) + " " + str(war(N, noami, ken))