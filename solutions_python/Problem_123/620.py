import sys

numcases = int(sys.stdin.readline())
for casenum in range(1,numcases+1):
    line = sys.stdin.readline().split()
    a = int(line[0])
    n = int(line[1])

    motes = [int(x) for x in sys.stdin.readline().split()]

    if a == 1:
        print ('Case #' + repr(casenum) + ': ' + str(n))
        continue

    motes.sort()

    result = 0
    s = a
    for j, mote in enumerate(motes):
        if s > mote:
            s += mote
        else:
            i = 0
            temps = s
            while temps <= mote:
                temps = temps+temps-1
                i += 1

            if i >= n - j:
                result += n - j
                break
            else:
                result += i
                s = temps+mote

    print ('Case #' + repr(casenum) + ': ' + str(result))