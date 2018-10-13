COLORS = ['R', 'O', 'Y', 'G', 'B', 'V']
for i in range(int(raw_input())):
    colors = map(int, raw_input().split())
    N = colors[0]
    colors = colors[1:]
    # small
    if colors[0] * 2 > N or colors[2] * 2 > N or colors[4] * 2 > N:
        s = "IMPOSSIBLE"
    else:
        ss = sorted(range(len(colors)), key=colors.__getitem__, reverse=True)
        sraw = [-1]*N
        curc = 0
        cur = ss[curc]
        j = 0
        NN = N
        while NN:
            while sraw[j%N] != -1:
                j+=1
            if not colors[cur]:
                curc += 1
                cur = ss[curc]
                if not colors[cur]:
                    break
            colors[cur] -=1
            sraw[j%N] = cur
            NN-= 1
            j+=2
            s = ""
        for k in sraw:
            s+= COLORS[k]
    print "Case #" + str(i + 1) + ": " + s
