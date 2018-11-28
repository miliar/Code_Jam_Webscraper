
def getNextLine(a):
    line = a.readline()
    return line.split()

if __name__ == "__main__":
    a = open("A-large.in")
    run_times = int(a.readline())

    for n in xrange(run_times):
        i,j = getNextLine(a)
        minimal = 2**int(i)
        k = int(j)

        if (k+1)%minimal == 0:
            value = "ON"
        else:
            value = "OFF"
        print "Case #" + str(n+1) + ": " + str(value)
    a.close()
