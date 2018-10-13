input = open("a.in" , "r")
output = open("a.out" , "w")

T = int(input.readline())

for i in range(1, T + 1):
    N = int(input.readline())
    S = []
    for _ in range(N):
        S.append(input.readline()[:-1])
    D = []
    for y in S:
        l = ""
        c = 0
        D.append([])
        for x in y:
            if x == l:
                c += 1
            else:
                if c > 0:
                    D[-1].append((l, c))
                c = 1
            l = x
        D[-1].append((l, c))
    if len(set([len(y) for y in D])) != 1:
        ans = "Fegla Won"
    else:
        f1 = True
        L = len(D[0])
        c = 0
        for j in range(L):
            if len(set([D[k][j][0] for k in range(N)])) != 1:
                f1 = False
                break
            mean = int(round(sum([D[k][j][1] for k in range(N)])/float(N)))
            for k in range(N):
                c += abs(mean - D[k][j][1])
        if f1:
            ans = str(c)
        else:
            ans = "Fegla Won"
    print ans
    output.write("Case #" + str(i) + ": " + ans + "\n")

input.close()
output.close()
