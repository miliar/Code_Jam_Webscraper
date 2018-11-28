import math
outfile = "output.txt"


def popinput(input):
    return int(input.readline().split()[0])

def inttolist(n):
    if n == 0:
        return []
    else:
        return inttolist(n / 10) + [n % 10]


def cycle(n, l):
    return n / 10 + (n % 10) * 10 ** l 

def recycs(n, a, b):
    l = len(inttolist(n)) - 1
    s = 0
    m = cycle(n, l)
    while m != n:
        if a <= n <= m <= b:
            s += 1
        m = cycle(m,l)
    return s

def sumprop(domain, prop):
    s = 0
    for i in domain:
        s += prop(i)
    return s

def solve(file):
    input = open(file, 'r')
    output = open(outfile, 'w')
    cases = popinput(input)
    for i in range(cases):
        output.write("Case #%(number)d: %(answer)s\n" % {"number":i + 1, "answer":solvecase(input)})

def solvecase(input):
    line = input.readline().split()
    a = int(line[0])
    b = int(line[1])
    return sumprop(range(a, b + 1), lambda x: recycs(x,a,b))

