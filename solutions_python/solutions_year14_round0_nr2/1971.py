
import fileinput

inp = fileinput.input()
def _():
    global inp
    return inp.readline()

T = int(_())
for case in range(T):
    case = str(case + 1)
    C, F, X = map(float, _().split())
    cps = 2.0
    t = 0
    while X / cps > C / cps + X / (cps + F):
        t += C / cps
        cps += F
    t += X / cps
    print "Case #" + case + ": " + str(t)