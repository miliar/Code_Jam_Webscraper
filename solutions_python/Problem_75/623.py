import sys


if __name__ == "__main__":

    f = open(sys.argv[1])
    testcount = int(f.readline())

    for testindex in range(0, testcount):

        line = f.readline()
        vals = line.strip().split()

        c = int(vals[0])
        del vals[0]
        combinations = dict()
        for i in range(0, c):
            combinations[(vals[i][0], vals[i][1])] = vals[i][2]
        del vals[0:c]

        d = int(vals[0])
        del vals[0]
        opposed = []
        for i in range(0, d):
            opposed.append((vals[i][0],vals[i][1]))
        del vals[0:d]

        n = int(vals[0])
        del vals[0]
        invocations = vals[0]

        elements = []
        for invocation in invocations:
            if not elements:
                elements.append(invocation)
                continue

            comb_found = False
            for comb in combinations.keys():
                if invocation == comb[0] and elements[-1] == comb[1] or invocation == comb[1] and elements[-1] == comb[0]:
                    elements[-1] = combinations[comb]
                    comb_found = True
                    break
            if comb_found:
                continue
            
            opp_found = False
            for opp in opposed:
                if invocation in opp:
                    for elem in elements:
                        if elem is not invocation and elem in opp:
                            opp_found = True
                            elements = []
                            break
            if opp_found:
                continue
            
            elements.append(invocation)

        elemstr = ""
        for idx, elem in enumerate(elements):
            if idx > 0:
                elemstr += ", " 
            elemstr += elem

        print "Case #%i: [%s]" % (testindex+1, elemstr)

