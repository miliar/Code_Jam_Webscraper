def flip(line, start, k):
    l = list(line)
    for i in range(start, start + k):
        c = l[i]
        l[i] = '-' if c == '+' else '+'
    return ''.join(l)

def solve(line, k):
    d = {}
    d[line] = 0
    for x in range(100):
        for state in d.keys():
            for i in range(0, len(line) - k + 1):
                flipped = flip(state, i, k)
                if flipped not in d:
                    d[flipped] = x + 1
    key= '+' * len(line)
    if key in d:
        return d[key]
    return 'IMPOSSIBLE'

def greedy_solve(line, k):
    temp = line
    score = 0
    for x in range(len(line) - k + 1):
        if temp[x] == '-':
            temp = flip(temp, x, k)
            score += 1
    if '-' in temp:
        return 'IMPOSSIBLE'
    return score

t = input()

for i in range(1, t+1):
    line, k = raw_input().strip().split()
#    print 'Case #{}: {}'.format(i, solve(line, int(k)))
    print 'Case #{}: {}'.format(i, greedy_solve(line, int(k)))
