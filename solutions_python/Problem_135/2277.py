
import sys

def main():
    f = open('A-small-attempt0.in')
#    f = sys.stdin
    tnum = int(f.readline())
    for t in range(1, tnum + 1):
        r = int(f.readline()) - 1
        s = set()
        for i in range(4):
            line = f.readline()
            if i == r:
                s = set([int(x) for x in line.split()])
        r = int(f.readline()) - 1
        for i in range(4):
            line = f.readline()
            if i == r:
                s &= set([int(x) for x in line.split()])
        if len(s) == 1:
            print "Case #%d: %d" % (t, s.pop())
        elif len(s) == 0:
            print "Case #%d: %s" % (t, "Volunteer cheated!")
        else:
            print "Case #%d: %s" % (t, "Bad magician!")

if __name__ == "__main__":
    main()
