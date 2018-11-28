
T = 0
originalT = 0
empty = False

def main():
    global T
    global empty
    global originalT
    f = open('A-small-attempt0.in','r')
    o = open('A-small-out.out','w')

    T = int(f.readline())
    originalT = T
    for line in f:
        testcase = line.split()
        r = int(testcase[0])
        t = int(testcase[1])
        discrim = ((2.0*r-1.0)*(2.0*r-1.0) + 8.0*t)**0.5
        first = -2.0*r + 1.0
        ringDrawn = int((first + discrim)/4.0)
        o.write('Case #' + str(abs(T - originalT) + 1) + ': ' + str(ringDrawn) + '\n')
        T -= 1
    f.close()
    o.close()

main()
