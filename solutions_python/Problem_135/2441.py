import sys

T = int(sys.stdin.readline().rstrip())

for caseno in range(T):
    fst = int(sys.stdin.readline().rstrip())
    grid1 = []
    for __ in range(4):
        grid1.append(map(int, sys.stdin.readline().split()))

    snd = int(sys.stdin.readline().rstrip())
    grid2 = []
    for __ in range(4):
        grid2.append(map(int, sys.stdin.readline().split()))

    intersection = set(grid1[fst - 1]) & set(grid2[snd - 1])

    if len(intersection) == 0:
        print "Case #%d: %s" % (caseno + 1, "Volunteer cheated!")
    elif len(intersection) == 1:
        print "Case #%d: %d" % (caseno + 1, intersection.pop())
    else:
        print "Case #%d: %s" % (caseno + 1, "Bad magician!")
