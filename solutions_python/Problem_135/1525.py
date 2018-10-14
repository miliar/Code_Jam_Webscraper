import sys

sys.stdin = open("input.in")
sys.stdout = open("output.txt", "w")
tn = int(sys.stdin.readline());

for ti in range(tn):
    r1 = int(sys.stdin.readline()) - 1;
    for i in range (4):
        line = sys.stdin.readline()
        if i == r1:
            s1 = set(line.split())
    r2 = int(sys.stdin.readline()) - 1;
    for i in range (4):
        line = sys.stdin.readline()
        if i == r2:
            s2 = set(line.split())

    #[r1] = [int(x) for x in sys.stdin.readline().split()];
    print "Case #%s:" % (ti + 1),
    s = s1.intersection(s2)
    if len(s) == 1:
        print s.pop()
    elif len(s) > 1:
        print "Bad magician!"
    else:
        print "Volunteer cheated!"
sys.stdout.close()
