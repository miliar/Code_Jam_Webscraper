
cases = int(input())
counter = 0


def flip(line, k):
    global counter
    if len(line) == 0:
        return []
    if len(line) < k:
        return None

    counter += 1
    return line[:-k] + [not x for x in line[-k:]]


# find '-+-', '+-+'??
for case in range(1, cases + 1):
    sample, k = input().split()
    line = [True if x == '+' else False for x in sample]
    counter = 0
    while line:
        while line and line[-1]:
            line.pop()
        line = flip(line, int(k))
    if line is None:
        print('Case #{}: {}'.format(case, 'IMPOSSIBLE'))
    else:
        print('Case #{}: {}'.format(case, counter))
