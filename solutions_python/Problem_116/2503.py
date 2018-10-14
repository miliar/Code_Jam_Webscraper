#!/usr/bin/env python
import sys

def main():
    data = [x.strip() for x in sys.stdin.readlines()]
    t = int(data.pop(0))
    for i in range(t):
        case = data[:4]
        case = case + ["".join(x) for x in  zip(*case)]
        dia1 = "".join([case[k][k] for k in range(4)])
        dia2 = "".join([case[k][3-k] for k in range(4)])
        case.append(dia1)
        case.append(dia2)
        inprog = False
        for j in range(len(case)):
            d = case[j].replace("T", "X")
            if "." in d:
                inprog = True
            if "XXXX" == d:
                print "Case #%d: X won" % (i+1)
                break
            d = case[j].replace("T", "O")
            if "OOOO" == d:
                print "Case #%d: O won" % (i+1)
                break
        else:
            if inprog:
                print "Case #%d: Game has not completed" % (i+1)
            else:
                print "Case #%d: Draw" % (i+1)

        data = data[5:]



if __name__ == '__main__':
    main()
