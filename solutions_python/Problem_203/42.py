inf = open('input.txt', mode='r')
outf = open('output.txt', mode='w')
cases = int(inf.readline())

for case in range(1, cases + 1):
    rstr = "Case #" + str(case) + ": "
    r, c = [int(x) for x in inf.readline().split()]
    lines = []
    kids = {}
    for i in range(r):
        lines.append(list(inf.readline().rstrip()))
        for j in range(c):
            if lines[i][j] != '?':
                kids[lines[i][j]] = (i, j)
    # print(lines)
    # print(kids)
    for kid, pos in kids.items():
        top = pos[0]
        bot = pos[0]
        right = pos[1]
        left = pos[1]
        while top - 1 >= 0 and lines[top - 1][pos[1]] == '?':
            top -= 1
        while bot + 1 < r and lines[bot + 1][pos[1]] == '?':
            bot += 1
        while right + 1 < c:
            check = True
            for i in range(top, bot + 1):
                if lines[i][right + 1] != '?':
                    check = False
            if not check:
                break
            right += 1

        while left - 1 >= 0:
            check = True
            for i in range(top, bot + 1):
                if lines[i][left - 1] != '?':
                    check = False
            if not check:
                break
            left -= 1

        for i in range(top, bot + 1):
            for j in range(left, right + 1):
                lines[i][j] = kid

    rstr += '\n'
    for line in lines:
        rstr += "".join(line) + '\n'
    print(rstr)
    outf.write(rstr + '\n')
