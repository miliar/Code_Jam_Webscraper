import sys


def run_case(casenum, infile):
    C, F, X = [float(x) for x in infile.readline().split()]
    t = 0.0
    rate = 2.0
    while True:
        time_to_X = (X / rate)
        time_to_farm = (C / rate)
        rate_with_farm = rate + F
        time_to_X_after_farm = (X / rate_with_farm)
        if (time_to_farm + time_to_X_after_farm) < time_to_X:
            t += time_to_farm
            rate = rate_with_farm
        else:
            t += time_to_X
            break

    print "Case #%d: %.7f" % (casenum, t)
    


infile = open(sys.argv[1], "r")

numcases = int(infile.readline())

for casenum in range(1, numcases + 1):
    run_case(casenum, infile)

