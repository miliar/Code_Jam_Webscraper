import sys

n_tests = int(sys.stdin.readline());
for i in range(n_tests):
    row1 = int(sys.stdin.readline().strip())
    sets1 = []
    for j in range(4):
        sets1.append(set([int(x) for x in sys.stdin.readline().split()]))
    row2 = int(sys.stdin.readline().strip())
    sets2 = []
    for j in range(4):
        sets2.append(set([int(x) for x in sys.stdin.readline().split()]))

    tset1 = sets1[row1-1]
    tset2 = sets2[row2-1]

    intersect = list(tset1.intersection(tset2))
    l = len(intersect)

    sys.stdout.write("Case #" + str(i+1) + ": ")
    if l == 0:
        sys.stdout.write("Volunteer cheated!")
    elif l == 1:
        sys.stdout.write(str(intersect[0]))
    else:
        sys.stdout.write("Bad magician!")
    print("")
