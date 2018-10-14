import sys

t = int(sys.stdin.readline())
def getSet():
    line = int(sys.stdin.readline())
    matrix = [[int(i) for i in sys.stdin.readline().split()] for i in range(4)]
    return set(matrix[line - 1])

for i in range(t):
    sys.stdout.write("Case #{0}: ".format(str(i + 1)))
    a = getSet()
    b = getSet()
    c = a & b
    if len(c) == 1:
        sys.stdout.write(str(list(c)[0]))
    elif len(c) == 0:
        sys.stdout.write("Volunteer cheated!")
    else:
        sys.stdout.write("Bad magician!")
    sys.stdout.write("\n")