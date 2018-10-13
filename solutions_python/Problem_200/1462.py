fin = open("B-large.in")
T = int(fin.readline())

fout = open('B_output.txt', 'w')
for t in range(1, T + 1):
    cN = fin.readline().strip()
    N = list(cN)
    pos = -1
    flag = True
    for i in range(len(N) - 1):
        if N[i] > N[i+1]:
            flag = False
            pos = i
            break
    if flag:
        fout.write("Case #%s: %s\n" % (t, ''.join(N)))
        continue
    while pos >= 0:
        if int(N[pos]) > 1:
            N[pos] = str(int(N[pos]) - 1)
            if pos == 0 or N[pos - 1] <= N[pos]:
                break
            else:
                pos -= 1
        else:
            pos -= 1

    for i in range(pos + 1, len(N)):
        N[i] = '9'
    if N[0] == '0' or int(''.join(N)) > int(cN):
        fout.write("Case #%s: %s\n" % (t, ''.join(N[1:])))
    else:
        fout.write("Case #%s: %s\n" % (t, ''.join(N)))
fout.close()