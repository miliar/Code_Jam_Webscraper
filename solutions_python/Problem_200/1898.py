import sys


"""
def build_matrix():
    m = {}
    for i in range(1, 11):
        m[1, i] = 10 - i
    for i in range(2, 20):
        m[i, 10] = 0
        for j in range(9, 0, -1):
            m[i, j] = m[i, j + 1] + m[i - 1, j]
    return m


m = build_matrix()
print(m)


def solve(n):
    return sum(m[i + 1, 1] for i in range(len(n))) - sum(m[i + 1, int(c) + 1] for i, c in enumerate(n[::-1]))


# print('\n'.join('Case #{}: {}'.format(i + 1, solve(l)) for i, l in enumerate(sys.stdin.readlines()[1:])))

print(solve('132'))
print(m[1, 1], m[2, 1], m[3, 1], m[1, 3], m[2, 2], m[3, 2])
print('\n'.join(['\t'.join(['({},{}): {:7}'.format(i, j, m[i, j]) for i in range(1, 20)]) for j in range(1, 10)]))
# for i in range(1, 20):
#     print(build(i))
"""


def solve(n):
    if len(n) == 1:
        return n
    n = [int(c) for c in n]
    should_repeat = True
    while should_repeat:
        should_repeat = False
        for i in range(1, len(n)):
            if n[i] < n[i - 1]:
                print(n[i])
                n = n[:i - 1] + [n[i - 1] - 1] + [9 for _ in n[i:]]
                should_repeat = True
                break
    return ''.join(map(str, n)).lstrip('0')


with open(r'D:\Downloads\B-large.in') as f, open(r'D:\Downloads\B-l.out', 'w') as out_f:
    print('\n'.join('Case #{}: {}'.format(i + 1, solve(l.strip())) for i, l in enumerate(f.readlines()[1:])), file=out_f)