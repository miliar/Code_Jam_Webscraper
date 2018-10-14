import fileinput

testcase = 1


lines = list(fileinput.input())

def doit():
    global lines
    global testcase

    row1 = int(lines.pop(0))
    grid1 = [{int(x) for x in lines.pop(0).split(" ")} for i in range(4)]
    row2 = int(lines.pop(0))
    grid2 = [{int(x) for x in lines.pop(0).split(" ")} for i in range(4)]

    intersection = grid1[row1-1].intersection(grid2[row2-1])

    if len(intersection) > 1:
        ans = "Bad magician!"
    elif not intersection:
        ans = "Volunteer cheated!"
    else:
        ans = list(intersection)[0]

    print "Case #%d: %s" % (testcase, ans)
    testcase += 1

Z = int(lines.pop(0))

for i in range(Z):
    doit()
