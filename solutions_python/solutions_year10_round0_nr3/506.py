
def runProg(R, k, grn, groups):
    pnt = 0 #group pointer
    euro = 0
    for i in xrange(R):
        start = pnt
        num = 0
        while True:
            if num + groups[pnt] <= k:
                num += groups[pnt]
                pnt += 1
                if pnt == grn:
                    pnt = 0
                if pnt == start:
                    break
            else:
                break
        euro += num
    return euro



def getNextLine(a):
    line = a.readline().split()
    for i in xrange(len(line)):
        line[i] = int(line[i])
    return line

if __name__ == "__main__":
    a = open("C-small-attempt2.in")
    b = open("cout.out", "w")
    run_times = int(a.readline())

    for n in xrange(run_times):
        this = getNextLine(a)
        groups = getNextLine(a)

        value = runProg(this[0], this[1], this[2], groups)
        #print "Case #" + str(n+1) + ": " + str(value)
        b.write("Case #" + str(n+1) + ": " + str(value)+"\n")
    b.close()
    a.close()
