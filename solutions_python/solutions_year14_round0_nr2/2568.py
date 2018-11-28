from math import ceil, floor

def time(n, c, f):
    t = 0;
    for a in xrange(n):
        t += c/(2+a*f)
    return t


def calculate(c, f, x, case):
    smallest = x/2
    if floor(x/c - 2/f) < 0:
        s = 0;
    else:
        s = int(floor(x/c - 2/f))
    for n in xrange(s,int(ceil(x/c - 2/f)) + 50):
        k = time(n, c, f) + x/(2+n*f)
        if k < smallest:
            smallest = k
    with open("output", "a") as myOutput:
        myOutput.write("Case #{}: {}\n".format(case,smallest))
        

def main():
    params = list()
    with open("input", "r") as myInput:
        p = int(myInput.readline())
        for a in xrange(p):
            params = myInput.readline().strip('\n').split(' ')
            c = float(params[0])
            f = float(params[1])
            x = float(params[2])
            calculate(c,f,x, a + 1)

main()