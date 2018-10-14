fin = open('B.in', 'r')
fout = open('B.out', 'w')


def generate_tidy(n):
    L = [int(d) for d in str(n)]
    if len(L) <= 1:
        return n
    L.reverse()
    new_tidy = []
    for i in range(len(L) - 1):
        if L[i] < L[i+1]:  # not increasing
            # everything before has to be 9
            new_tidy = [9 for j in range(i+1)]
            L[i+1] -= 1
        else:
            new_tidy.append(L[i])
    new_tidy.append(L[-1])
    new_tidy = map(str, new_tidy)
    new_tidy.reverse()
    return int(''.join(new_tidy))


T = int(fin.readline())
for t in range(1, T+1):
    N = int(fin.readline())
    ans = str(generate_tidy(N))
    fout.write('Case #' + str(t) + ': ' + ans + '\n')
