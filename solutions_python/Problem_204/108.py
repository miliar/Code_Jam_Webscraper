import math
fin = open('B-large.in', 'r')
fout = open('output.txt', 'w')
T = int(fin.readline())
for cID in range(T):
    print(cID)
    Nstr, Pstr = fin.readline().strip().split()
    N = int(Nstr)
    P = int(Pstr)
    R = [int(x) for x in list(fin.readline().strip().split())]
    packages = []
    for i in range(N):
        p = [int(x) for x in list(fin.readline().strip().split())]
        packages.append(p)
    cans = []
    for i in range(N):
        cans.append([])
        for j in range(len(packages[i])):
            r = math.floor(packages[i][j] / R[i] / 0.9)
            l = math.ceil(packages[i][j] / R[i] / 1.1)
            if l <= r:
                cans[i].append((l,r))
        cans[i].sort()
    ptr = [0 for i in range(N)]
    valid = True
    cnt = 0
    for i in range(N):
        if len(cans[i]) == 0:
            valid = False
    while valid:
        flag = True
        minV = cans[0][ptr[0]]
        minIdx = 0
        overlap = list(cans[0][ptr[0]])
        for i in range(N):
            if cans[i][ptr[i]][0] > overlap[1] or cans[i][ptr[i]][1] < overlap[0]:
                flag = False
                break
            else:
                overlap[0] = max(overlap[0], cans[i][ptr[i]][0])
                overlap[1] = min(overlap[1], cans[i][ptr[i]][1])
        if not flag:
            for i in range(N):
                if cans[i][ptr[i]][1] < minV[0]:
                    minV = cans[i][ptr[i]]
                    minIdx = i
            ptr[minIdx] += 1
            if ptr[minIdx] >= len(cans[minIdx]):
                valid = False
                break
        else:
            cnt += 1
            for i in range(N):
                ptr[i] += 1
                if ptr[i] >= len(cans[i]):
                    valid = False
                    break
    fout.write("Case #{}: {}\n".format(cID+1, cnt))

