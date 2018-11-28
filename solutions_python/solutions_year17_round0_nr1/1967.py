def flip(s, index):
    lst = list(s)
    if lst[index] == '-':
        lst[index] = '+'
    else:
        lst[index] = '-'
    return "".join(lst)


fin = open('pancake.in', 'r')
fout = open('pancake.out', 'w')

T = int(fin.readline().strip())

for t in range(T):
    line = fin.readline().split()
    S = line[0]
    K = int(line[1])

    count = 0

    n = len(S)
    for i in range(n-K+1):
        if S[i] == '-':
            for j in range(K):
                S = flip(S, i+j)
            count = count + 1
    if '-' in S:
        fout.write("Case #" + str(t+1) + ": IMPOSSIBLE\n")
    else:
        fout.write("Case #" + str(t+1) + ": " + str(count) + "\n")

fin.close()
fout.close()
