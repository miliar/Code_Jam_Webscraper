from sortedcontainers import SortedList


def solve(n, k):
    divisions = SortedList()
    divisions.add(n)
    for i in range(k):
        x = divisions.pop()
        res = (int((x - 1) / 2), x - 1 - int((x - 1) / 2))
        divisions.add(res[0])
        divisions.add(res[1])
    return max(res), min(res)


with open(r'D:\Downloads\C-small-1-attempt0.in') as f, open(r'D:\Downloads\C.out', 'w') as out_f:
    print('\n'.join('Case #{}: {} {}'.format(i + 1, *solve(*map(int, l.strip().split()))) for i, l in enumerate(f.readlines()[1:])), file=out_f)