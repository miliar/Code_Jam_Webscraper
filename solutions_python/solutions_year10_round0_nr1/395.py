import sys
def spanner(n, k):
    binaryString = bin(k)
    binaryMasked = binaryString[-n:]

    return (binaryMasked == n*"1")

def parse(filename):
    f = open(filename,"r")
    numcases = int(f.readline())

    for i in range(1,numcases+1):
        line = f.readline().split()
        n = int(line[0])
        k = int(line[1])
        print "Case #" + str(i) + ": ",
        if (spanner(n,k)):
            print "ON"
        else:
            print "OFF"


parse(sys.argv[1])
