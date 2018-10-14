import math

f = open("input_smallB.txt", "r")
text  = f.readlines()

first = text[0].rstrip('\n').split(' ')
T = int(first[0])

lineNum = 1
case = 1
for i in range(T):
    split = text[lineNum].rstrip('\n').split(' ')
    lineNum+=1
    N = int(split[0])
    P = int(split[1])


    split = text[lineNum].rstrip('\n').split(' ')
    lineNum+=1

    R = [0] * N
    for j in range(N):
        R[j] = int(split[j])

    Q = [[0 for j in range(P)] for x in range(N)]
    uses = [[0 for j in range(P)] for x in range(N)]
    
    numeach = [{} for j in range(N)]
    for j in range(N):
        split = text[lineNum].rstrip('\n').split(' ')
        lineNum+=1
        for k in range(P):
            Q[j][k] = int(split[k])
            serves = int(round(float(Q[j][k])/float(R[j])))
            for l in range(0, serves*2):
                target = float(l) * float(R[j])
                if Q[j][k] >= int(math.ceil(target*0.9)) and Q[j][k] <= int(math.floor(target*1.1)):
                    if l not in numeach[j]:
                        numeach[j][l] = []
                    numeach[j][l].append(k)
                    uses[j][k] += 1
    
    kits = 0

    used = [[False for j in range(P)] for x in range(N)]

    #print numeach
    for servings in numeach[0].keys():
        m = 100000000000
        for j in range(N):
            if servings not in numeach[j]:
                m = 0
            else:
                mc = 0
                for v in numeach[j][servings]: 
                    if not used[j][v]:
                        mc += 1
                m = min(m, mc)

        for j in range(N):
            idx = 0
            k = 0
            while k < m:
                v = numeach[j][servings][idx]
                if not used[j][v]:
                    used[j][v] = True
                    k += 1
                idx += 1

        if m < 100000000000:
            kits += m

    print "Case #{}: {}".format(case, kits)
    case += 1
    #iterate and determine number of 
        
    
