f = open("A-large.in")
fOut = open("A-large.out", "w")

readIntVec = lambda f: [int(x) for x in f.readline().strip().split()]

T = int(f.readline().strip())

for tc in range(T):
    N, K = readIntVec(f)
    ans = "ON"
    for i in range(N):
        if (K & (1 << i)) == 0:
            ans = "OFF"
            break

    outLine = "Case #%d: %s" % (tc + 1, ans)
    fOut.write(outLine + "\n")
    #print outLine
    

fOut.close()
f.close()
