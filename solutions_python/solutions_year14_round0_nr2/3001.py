import sys

lines = []
for line in sys.stdin.readlines():
    lines.append(line)

tc = int(lines[0])

for i in range(1, tc+1):
    c, f, x = [float(item) for item in lines[i].split(' ')]
    current_f = 2.0
    sol = 0

    while x/current_f > c/current_f + x/(current_f+f):
        sol += c/current_f
        current_f += f
    else:
        sol += x / current_f
    print 'Case #{}: {}'.format(i, sol)
