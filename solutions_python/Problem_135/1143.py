import sys

def get_line(lines, i):
    a = int(lines[i])
    return lines[i + a].split()

lines = sys.stdin.readlines()
T = int(lines[0])
i = 1
for t in range(T):
    l1 = get_line(lines, i)
    i += 5
    l2 = get_line(lines, i)
    i += 5
    e = set(l1) & set(l2)
    if len(e) > 1:
        print('Case #{}: Bad magician!'.format(t + 1))
    elif len(e) == 1:
        print('Case #{}: {}'.format(t + 1, list(e)[0]))
    else:
        print('Case #{}: Volunteer cheated!'.format(t + 1))

