with open("A-large.in") as fin:
    with open("A.out", "w") as fout:
        T = int(fin.readline())
        for q in range(T):
            vals = fin.readline().strip().split(" ")
            #print(vals)
            sequence = list()
            for s in range(int(vals[0])):
                sequence.append((vals[s * 2 + 1], vals[s * 2 + 2]))
            o = b = 1
            o1 = b1 = 0
            t = 0
            for i in range(len(sequence)):
                n = int(sequence[i][1])
                if sequence[i][0] == "O":
                    dt = max(abs(n - o) - b1, 0) + 1
                    #print(dt)
                    t += dt
                    o1 += dt
                    b1 = 0
                    o = n
                else:
                    dt = max(abs(n - b) - o1, 0) + 1
                    #print(dt)
                    t += dt
                    b1 += dt
                    o1 = 0
                    b = n
            fout.write("Case #" + str(q + 1) + ": " + str(t) + "\n")
