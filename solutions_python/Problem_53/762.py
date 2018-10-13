def main():
    ifile = open("input.txt", 'r')
    ofile = open("output.txt", 'w')

    #get the number of cases
    numcases = int(ifile.readline())

    for n in range(numcases):
        N,K = ifile.readline().split(" ")
        N,K = int(N),int(K)
        ans = solve(N,K)
#        if ans is not verify(N,K):
#            print "WRONG: #",n+1
        if ans:
            ofile.write("Case #%s: ON\n" % (n+1))
        else:
            ofile.write("Case #%s: OFF\n" % (n+1))

    ifile.close()
    ofile.close()

def solve(N,K):
    if K is 0:
        return False
    wraparound = 2**N
    Kmod = K % wraparound
    if Kmod is (2**N-1):
        return True
    else:
        return False

def verify(N,K):
    if K is 0:
        return False
    snappers = [False for n in range(N)]
    for k in range(K):
        for i,s in enumerate(snappers):
            if i is 0:
                snappers[i] = not snappers[i]
            elif snappers[i-1]:
                break
            else:
                snappers[i] = not snappers[i]
    allOn = True
    for s in snappers:
        if not s:
            allOn = False
            break
    return allOn

if __name__ == "__main__":
    main()
