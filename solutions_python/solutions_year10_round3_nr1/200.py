def p2d(tab):
    for e in tab:
        print(e)

if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)

    for test in range(N):
        total = 0
        l = fin.readline().replace("\n", "")
        n = int(l)
        conns = []

        for i in range(n):
            l = fin.readline().replace("\n", "").split(" ")
            conns.append([int(l[0]), int(l[1])])

        conns.sort(key=lambda c: c[0])

        #print conns

        for i in range(len(conns)):
            for j in range(len(conns)):
                #print "cmp", conns[i], conns[j], " => ", conns[j][0] > conns[i][0], conns[j][1] < conns[i][1]
                if conns[i][0] < conns[j][0] and conns[i][1] > conns[j][1]:
                    total += 1

        sol = "Case #" + str(test+1) + ": " + str(total) + "\n"
        print(sol)
        fout.write(sol)