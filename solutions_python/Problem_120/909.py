from math import floor, sqrt

def calculate_rings(case):
    r = case[0]
    t = case[1]
    return int(floor((-2 * r + 1 + sqrt(4 * r * r - 4 * r + 1 + 8 * t)) / 4.0))

name = "A-small-attempt0"
f = open(name + ".in", "r")
line_num = 0
cases = {}

for line in f:
    line_num += 1
    if line_num > 1:
        cases[line_num - 1] = [int(i) for i in line.split()]

f.close()
g = open(name + ".out", "w")

for i in range(1, line_num):
    g.write("Case #" + str(i) + ": " + str(calculate_rings(cases[i])) + "\n")

g.close()