import fileinput

get = lambda t: list(t(i) for i in input.readline().strip().split())


def solve_case():
    R, C, W = get(int)
    ans = C//W
    if C%W != 0:
        ans += 1
    ans += W-1
    ans *= R
    return ans
    


with fileinput.input() as input:
    T, = get(int)
    for c in range(T):
        print('Case #%s: %s' % (c+1, solve_case()))


