import fileinput

inp = fileinput.input()
next(inp)

i = 1
for line in inp:
    c, f, x = (float(x) for x in line.split(' '))
    r, res = 2.0, 0
    while x / r > c / r + x / (r + f):
        r, res = r + f, res + c / r

    print('Case #{0}: {1:.7f}'.format(i, res + x / r))
    i += 1
