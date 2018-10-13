
 # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    x, n = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    n = int(n)
    repl = 0
    for xi in range(0, len(x) - n + 1):
        if x[xi] == '-':
            repl += 1
            for xk in range(xi, xi + n):
                if x[xk] == '-': x = x[:xk] + '+' + x[xk + 1:]
                else: x = x[:xk] + '-' + x[xk + 1:]

    res = ''
    if x.count('+') == len(x):
        res = repl
    else:
        res = 'IMPOSSIBLE'

    print('Case #{}: {}'.format(i, res))


  # check out .format's specification for more formatting options
