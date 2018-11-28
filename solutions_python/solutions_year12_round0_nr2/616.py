outfile = "output.txt"

def popinput(input):
    return int(input.readline().split()[0])


def solve(file):
    input = open(file, 'r')
    output = open(outfile, 'w')
    cases = popinput(input)
    for i in range(cases):
        output.write("Case #%(number)d: %(answer)s\n" % {"number":i + 1, "answer":solvecase(input)})

def solvecase(input):
    line = input.readline().split()
    n = int(line[0])
    s = int(line[1])
    p = int(line[2])
    scores = map(int, line[3:])
    return most(n,s,p,scores)


def most(n,s,p,scores):
    if p == 0:
        return n
    elif p == 1:
        return len(filter(lambda x: x >= 1, scores))
    else:
        normals = len(filter(lambda x: x >= 3*p -2, scores))
        surprises = min(s, len(filter(lambda x: 3*p - 2 > x >= 3 * p - 4, scores)))
        return normals + surprises

