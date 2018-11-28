import os

if __name__ == "__main__":
    fin = open("B-small-attempt0.in", "r")
    fout = open("B.out", "w")
    T = int(fin.readline())
    for t in range(T):
        t += 1
        C, F, X = [float(x) for x in fin.readline().strip().split()]
        mincost = -1
        i = 0
        while True:
            cost = 0
            for j in range(i):
                cost += C / (2+j*F)
            cost += X / (2 + i * F)
            if mincost == -1 or cost < mincost:
                if mincost != -1 and mincost - cost < 0.00000001:
                    break
                mincost = cost
            else:
                break
            i += 1
        fout.write("Case #%d: %s\n" % (t, mincost))
    fout.close()

