with open('A-large.in') as fin:
    T = int(fin.readline().split()[0])
    print(T)
    patterns = []
    flippers = []
    for i in range(T):
        dataIn = fin.readline().split()
        patterns.append(dataIn[0])
        flippers.append(int(dataIn[1]))

flipsOut = []
for i in range(T):
    pat = list(patterns[i])
    k = flippers[i]
    flips = 0
    for j in range(len(pat) - k + 1):
        if '+' == pat[j]:
            continue
        flips += 1
        for l in range(j, j + k):
            if '+' == pat[l]:
                pat[l] = '-'
            else:
                pat[l] = '+'
    for j in range(len(pat) - k + 1, len(pat)):
        if '-' == pat[j]:
            flips = -1
            break
    flipsOut.append(flips)

with open('pancake_out.txt', 'w') as fout:
    for i in range(T):
        fout.write('Case #' + str(i + 1) + ': ')
        if flipsOut[i] >= 0:
            fout.write(str(flipsOut[i]) + '\n')
        else:
            fout.write('IMPOSSIBLE\n')
