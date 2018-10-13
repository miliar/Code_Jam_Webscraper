infile = open('A-large.in', 'r')
outfile = open('pancake.out', 'w')


def flip(pancakes):
    """Flip the pancakes from +/- to -/+"""
    res = ''
    for pancake in pancakes:
        if pancake == '+':
            res += '-'
        else:
            res += '+'
    return res

T = int(infile.readline())

for t in range(1, T + 1):
    pancakes, flipper = infile.readline().strip().split()

    flipper = int(flipper)

    res = 0
    for i in range(len(pancakes) - flipper):
        if pancakes[i] == '+':
            continue
        else:
            pancakes = pancakes[:i] + flip(pancakes[i:i + flipper]) + pancakes[i + flipper:]
            res += 1

    if pancakes[-flipper:] == '-' * flipper:
        res += 1
    elif pancakes[-flipper:] != '+' * flipper:
        res = 'IMPOSSIBLE'

    outfile.write('Case #{0}: {1}'.format(t, res) + '\n')
