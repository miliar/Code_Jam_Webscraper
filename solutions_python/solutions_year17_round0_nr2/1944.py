import sys
read = lambda f=int: map(f, sys.stdin.readline().split())
T, = read()
def solve(xs):
    i = 0
    while i+1 != len(xs) and xs[i] <= xs[i+1]:
        i += 1
    if i+1 == len(xs):
        return xs
    # xs[i] > xs[i+1]
    while i != 0 and xs[i-1] > xs[i]-1:
        i -= 1
    if i == 0 and xs[0] == 1:
        return [9]*(len(xs)-1)
    # xs[i-1] <= xs[i]-1
    return xs[:i] + [xs[i]-1] + [9]*(len(xs)-i-1)

for case in range(T):
    xs = list(map(int,sys.stdin.readline().strip()))
    res = ''.join(map(str, solve(xs)))
    print('Case #{}: {}'.format(case+1, res))

