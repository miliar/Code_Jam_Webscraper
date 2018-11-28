import sys

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        firstAnswer = int(sys.stdin.readline())
        firstArrange = [[]]
        for i in range(4):
            firstArrange.append(map(int,sys.stdin.readline().strip().split()))
        secondAnswer = int(sys.stdin.readline())
        secondArrange = [[]]
        for i in range(4):
            secondArrange.append(map(int,sys.stdin.readline().strip().split()))
        intersect = set(firstArrange[firstAnswer]) & set(secondArrange[secondAnswer])
        if len(intersect) == 1:
            print "Case #%d: %d" % (t+1, intersect.pop())
        elif len(intersect) > 1:
            print "Case #%d: %s" % (t+1, "Bad magician!")
        elif len(intersect) < 1:
            print "Case #%d: %s" % (t+1, "Volunteer cheated!")
