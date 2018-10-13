import sys

def main(fName):
    f = open(fName, "r")
    cases = int(f.readline())
    for caseNum in xrange(cases):
        existing, toCreate = map(int, f.readline().split())
        directories = set()
        counter = 0
        for i in xrange(existing):
            path = f.readline().strip()
            parts = path.split('/')
            for j in xrange(2, len(parts) + 1):
                directories.add("/".join(parts[:j]))
        for i in xrange(toCreate):
            path = f.readline().strip()
            parts = path.split('/')
            for j in xrange(2, len(parts) + 1):
                p = "/".join(parts[:j])
                if p not in directories:
                    counter += 1
                    directories.add(p)
        print "Case #%d: %d" % (caseNum + 1, counter)
    f.close()

main(sys.argv[1])