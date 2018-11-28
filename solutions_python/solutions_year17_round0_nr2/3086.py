import sys

fname = sys.argv[1]
output = open(sys.argv[1] + ".out", 'w')

def solve(number):
    xsorted, xunsorted = compute(map(int, number))
    while xunsorted != []:
        xunsorted = [9] * len(xunsorted)
        xsorted[-1] = xsorted[-1] - 1
        xsorted, xunsorted = compute(xsorted + xunsorted)
    return xsorted

def compute(n):
    for i in range(1, len(n)):
        if(n[i] < n[i-1] ):
            return n[:i], n[i:]
    return n, []

with open(fname) as f:
    content = f.readlines()

line = [x.strip() for x in content]

for i in range(1, int(line[0]) + 1):
    solution = int("".join(map(str, solve(line[i]))))
    output.write("Case #" + str(i) + ": " + str(solution) + "\n")
