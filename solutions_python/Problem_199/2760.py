lines = open('A-large.in', 'r').read().strip().split('\n')
T = int(lines[0])

def flip_pat(pat, i, k):
    if i + k > len(pat):
        return pat

    for x in range(k):
        if pat[i + x] == '+':
            pat = pat[:i+x] + '-' + pat[i+x+1:]
        else:
            pat = pat[:i+x] + '+' + pat[i+x+1:]

    return pat

def solveit(pat, k):
    cnt = 0
    for i, x in enumerate(pat):
        if pat[i] == '-':
            pat = flip_pat(pat, i, k)
            cnt += 1


    for x in pat:
        if x == '-':
            cnt = -1
            break

    return cnt


for i, line in enumerate(lines[1:]):
    res = solveit(line.split()[0], int(line.split()[1]))
    print 'Case #' + str(i+1) + ':',
    print res if (res >= 0) else 'IMPOSSIBLE'
