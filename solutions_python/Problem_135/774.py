def getans(row):
    for i in range(4):
        if i == row:
            ans = file.readline().split()
            ans[3] = ans[3].replace("\n","")
        else:
            file.readline()
    return ans

with open('A-small-attempt0.in') as file:
    cases = int(file.readline())
    output = open('output.txt','w')
    for c in range(1, cases + 1):
        row1 = int(file.readline()) - 1
        ans1 = set(getans(row1))
        row2 = int(file.readline()) - 1
        ans2 = set(getans(row2))
        p = tuple(set.intersection(ans1, ans2))
        if len(p) == 0:
            output.write('Case #%d: Volunteer cheated!\n' % c)
        elif len(p) == 1:
            output.write('Case #%d: %s\n' % (c, p[0]))
        elif len(p) > 1:
            output.write('Case #%d: Bad magician!\n' % c)
