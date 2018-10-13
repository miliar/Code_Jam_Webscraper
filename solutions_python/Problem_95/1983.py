import sys

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', "z":"q"}

def main(fName):
    f = open(fName, "r")
    cases = int(f.readline())
    for i in xrange(cases):
        caseNo = i + 1
        line = f.readline().strip()
        translation = "".join(map(lambda c: d[c], line))
        print "Case #%d: %s" % (caseNo, translation)

if __name__ == "__main__":
    main(sys.argv[1])
