import sys

def main(fName):
    f = open(fName, "r")
    cases = int(f.readline())
    for i in xrange(cases):
        noOfSnappers, fingerSnaps = map(int, f.readline().split())
        p = 2 ** noOfSnappers
        isOn = fingerSnaps % p == p - 1
        print "Case #%d: %s" % (i + 1, "ON" if isOn else "OFF")
        

main(sys.argv[1])