fin = open('A-small-attempt0.in','r')

lines = fin.readlines()

T = int(lines.pop(0))
for i in range(T):
    r1 = int(lines.pop(0))
    for r in range(4):
        line = lines.pop(0)
        if r+1 == r1:
            s1 = {int(x) for x in line.split()}

    r2 = int(lines.pop(0))
    for r in range(4):
        line = lines.pop(0)
        if r+1 == r2:
            s2 = {int(x) for x in line.split()}

    ans = list(s1 & s2)
    n = len(ans)
    if n == 1:
        print "Case #" + str(i+1) + ": " + str(ans[0])
    elif n >= 2:
        print "Case #" + str(i+1) + ": " + "Bad magician!"
    else:
        print "Case #" + str(i+1) + ": " + "Volunteer cheated!"


