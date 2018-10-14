from sys import stdin

cases = int(stdin.readline())

for t in range(cases):
    num = int(stdin.readline())
    line = ""
    for i in range(1,5):
        if i == num:
            line = stdin.readline()
        else:
            stdin.readline()
    line = set([int(n) for n in line.split()])

    num2 = int(stdin.readline())
    line2 = ""
    for i in range(1,5):
        if i == num2:
            line2 = stdin.readline()
        else:
            stdin.readline()
    line2 = set([int(n) for n in line2.split()])
    intersection = line.intersection(line2)
    if len(intersection) == 0:
        print("Case #%d: Volunteer cheated!" % (t+1))
    elif len(intersection) > 1:
        print("Case #%d: Bad Magician!" % (t+1))
    else:
        print("Case #%d: %d" % ((t+1), list(intersection)[0]))
