import sys, math

def calculate(r, t):
    p = float(r / 2) - 0.25
    count = math.floor( math.sqrt(t/2.0 + p * p) -  p)
    if float(p) == float(r/2):
        count = count - 1
    return int(count)

T = int(sys.stdin.readline())

count = 1

while count <= T:
    [r, t] = [ float(x) for x in sys.stdin.readline().strip().split(" ")]

    print "Case #" + str(count) + ": " + str(calculate(r, t))
    count = count + 1
