import fileinput

testcase = 1


lines = list(fileinput.input())

def doit():
    global lines
    global testcase

    C, F, X = [float(x) for x in lines.pop(0).split(" ")]

    rate = 2.0
    T = 0

    while T + (X / rate) > T + (C / rate) + (X / (rate + F)):
        T += C / rate
        rate += F

    print "Case #%d: %.7f" % (testcase, T + (X / rate))
    testcase += 1

Z = int(lines.pop(0))

for i in range(Z):
    doit()
