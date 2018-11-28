import sys

def main() :
    lines = sys.stdin.readlines()
    cases = int(lines[0])
    for case in xrange(1,cases+1) :
        num = int(lines[2*case-1])
        line = map(int,lines[2*case].split())
        xorVal = 0
        for i in xrange(num) :
            xorVal = xorVal ^ line[i]
        print "Case #" + str(case) + ":",
        if xorVal == 0 :
            print sum(line) - min(line)
        else :
            print "NO"

main()
