#!/usr/bin/env python

from sys import argv

def elements(comb, opp, invoke):
    if invoke[0] in opp:
        last_opp = [invoke[0]]
    else:
        last_opp = []

    j = 0
    cleared = False
    elements = [invoke[0]]
    for ei in invoke[1:]:

        # Try to get the next element
        try:
            ej = elements[j]
        except IndexError:
            ej = None

        if (ei, ej) in comb:
            elements[j] = comb[(ei, ej)]
            try:
                last_opp.remove(ej)
            except ValueError:
                pass
            continue
        elif len(last_opp) > 0:
            for ek in last_opp:
                if opp[ek] == ei:
                    # Clear element list
                    cleared = True
                    break
            if cleared:
                j = -1
                elements = []
                last_opp = []
                cleared = False
                continue

        if ei in opp:
            last_opp.append(ei)

        elements.append(ei)
        j = j + 1

    return ", ".join(elements)


if __name__ == "__main__":
    with open(argv[1], "r") as f:
        cases = int(f.readline())
        for i in range(cases):
            line = f.readline().split()
            opp = {}
            comb = {}
            idx = 0
            c = int(line[idx])
            for _ in range(c):
                idx = idx + 1
                comb.update({(line[idx][0], line[idx][1]): line[idx][2]})
                comb.update({(line[idx][1], line[idx][0]): line[idx][2]})
            idx = idx + 1
            d = int(line[idx])
            for _ in range(d):
                idx = idx + 1
                opp.update({line[idx][0]: line[idx][1]})
                opp.update({line[idx][1]: line[idx][0]})
            invoke = [char for char in line[idx + 2]]
            print "Case #%d: [%s]" % (i + 1, elements(comb, opp, invoke))
