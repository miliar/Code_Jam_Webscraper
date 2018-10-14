import sys

fh = open(sys.argv[1])
T = int(fh.readline())
for i in range(T):
    r1 = int(fh.readline())
    cards1 = []
    for j in range(4):
        cards1.append(map(int, fh.readline().rstrip().split(" ")))
    r2 = int(fh.readline())
    cards2 = []
    for j in range(4):
        cards2.append(map(int, fh.readline().rstrip().split(" ")))
    answer = set(cards1[r1-1]).intersection(cards2[r2-1])
    if len(answer) == 0:
        y = "Volunteer cheated!"
    if len(answer)==1:
        y = answer.pop()
    elif len(answer) > 1:
        y = "Bad magician!"
    print "Case #{0}: {1}".format(i+1, y)
