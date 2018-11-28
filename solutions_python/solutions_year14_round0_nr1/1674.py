import sys

def calculate(lines):
    m = int(lines[0]) - 1
    set1 = [set(lines[1+i].split()) for i in range(4)][m]
    n = int(lines[5]) - 1
    set2 = [set(lines[6+i].split()) for i in range(4)][n]
    result = set1.intersection(set2)
    if not result:
        return "Volunteer cheated!"
    if len(result) > 1:
        return "Bad magician!"
    return result.pop()

lines = sys.stdin.readlines()
ncase = int(lines[0])
lines = lines[1:]
for i in range(1, ncase+1):
    print "Case #%d:"%i, calculate(lines)
    lines = lines[10:]
