fin = open("A-large.in", 'r')
fout = open("output.out", 'w')
def wp(n,lines,t):
    os = 0
    ls = 0
    for i in range(len(lines[n])):
        if t == -1 or i != t:
            if lines[n][i] == '0': os += 1
            if lines[n][i] == '1': ls += 1
    return float(ls) / (ls + os)
def owp(n, lines):
    tot = 0.0
    op = []
    for i in range(len(lines[n])):
        if lines[n][i] == '0' or lines[n][i] == '1': op.append(i)
    for j in op:
        tot += wp(j, lines, n)
    return tot / len(op)
def oowp(n, lines):
    tot = 0.0
    op = []
    for i in range(len(lines[n])):
        if lines[n][i] == '0' or lines[n][i] == '1': op.append(i)
    for j in op:
        tot += owp(j, lines)
    return tot / len(op)
T = int(fin.readline())
for i in range(T):
    N = int(fin.readline())
    lines = []
    for j in range(N):
        lines.append(fin.readline())
    s = 'Case #' + str(i+1) + ':' + '\n'
    fout.write(s)
    for k in range(N):
        s = str(0.25*wp(k,lines,-1)+0.5*owp(k,lines)+0.25*oowp(k,lines)) + '\n'
        fout.write(s)
print 'done'
fin.close()
fout.close()
