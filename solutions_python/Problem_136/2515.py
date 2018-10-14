import sys
import collections


TestCase = collections.namedtuple('TestCase', ['tid','c', 'f', 'x'])


def read_line():
    return sys.stdin.readline().strip()

def read_inputs():
    n_tests = int(read_line())
    tests = []
    for case_id in range(1, n_tests + 1):
        c, f, x = map(float, read_line().split())
        tests.append(TestCase(case_id, c, f, x))

    return tests

def solve(tid, c, f, x):
    fi = 2.0
    def build_time(n):
        return sum(c / (fi + k *f) for k in range(n))

    def farm_time(n):
        return x / (fi + n * f)

    def total_time(n):
        return build_time(n) + farm_time(n)
    n1 = max(int((x*f - c*(fi +f)) / (c*f)), 0)
    n2 = n1 + 1
    n = min([n1, n2], key=total_time)
    ans = total_time(n)
    return 'Case #{}: {}'.format(tid, ans)

tcs = read_inputs()
for tc in tcs:
    print(solve(*tc))
