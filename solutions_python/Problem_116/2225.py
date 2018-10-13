import sys

px = ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']
po = ['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO']

finput = open(sys.argv[1], 'r')
foutput = open('output', 'w')

cases = []
n = int(finput.readline())
for i in range(n):
    temp = []
    for j in range(5):
        line = finput.readline()[:-1]
        if(line):
            temp.append(line)
    cases.append(temp)

    digl = "%s%s%s%s" % (cases[i][0][0], cases[i][1][1], cases[i][2][2], cases[i][3][3])
    digr = "%s%s%s%s" % (cases[i][0][3], cases[i][1][2], cases[i][2][1], cases[i][3][0])
    for k in range(4):
        vertical = "%s%s%s%s" % (cases[i][0][k], cases[i][1][k], cases[i][2][k], cases[i][3][k])
        cases[i].append(vertical)
    cases[i].append(digl)
    cases[i].append(digr)

for n, c in enumerate(cases):
    nf = False
    done = False
    for x in c:
        if x in px:
            foutput.write("Case #%d: X won\n" % (n + 1))
            done = True
            break
        elif x in po:
            foutput.write("Case #%d: O won\n" % (n + 1))
            done = True
            break
        if '.' in x:
            nf = True
    if (not done) and nf:
        foutput.write("Case #%d: Game has not completed\n" % (n + 1))
    if (not done) and (not nf):
        foutput.write("Case #%d: Draw\n" % (n + 1))

finput.close()
foutput.close()