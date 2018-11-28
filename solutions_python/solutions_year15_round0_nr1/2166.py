import fileinput

def solve(n):
    acc = 0
    add = 0
    for i, x in enumerate(n, 1):
        acc += x
        if acc < i:
            add += i - acc
            acc = i
    return add

for case, line in enumerate(fileinput.input()):
    if case == 0:
        continue
    n, b = line.split(' ')
    print("Case #%d: %d" % (case, solve([int(x) for x in b.strip()])))
