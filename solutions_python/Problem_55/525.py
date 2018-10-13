def p2d(tab):
    for e in tab:
        print(e)

def tar(q, k):
    sum = 0
    for g in range(len(q)):
        if sum + q[g] <= k: sum += q[g]
        else: break
    return (sum, g)

if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)

    for test in range(N):
        total = 0
        l = fin.readline().replace("\n", "")
        r, k, n = (int(v) for v in l.split(" "))
        l = fin.readline().replace("\n", "")
        q = [int(g) for g in l.split(" ")]

        #print "r k n q"
        #print r, k, n, q

        for i in range(r):
            sum, g = tar(q, k)
            total += sum
            q = q[g:] + q[:g]
            pass

        sol = "Case #" + str(test+1) + ": " + str(total) + "\n"
        print(sol)
        fout.write(sol)
