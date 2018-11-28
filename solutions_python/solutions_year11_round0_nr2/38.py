#!/usr/bin/python

import sys


def magicka(testcase):
    arr = testcase.split()
    C = int(arr[0])
    combine_formula = {}
    for i in range(1, 1 + C):
        combine_formula[(arr[i][0], arr[i][1])] = arr[i][2]
        combine_formula[(arr[i][1], arr[i][0])] = arr[i][2]

    oppose_formula = {}
    D = int(arr[1 + C])
    for i in range(1 + C + 1, 1 + C + 1 + D):
        if oppose_formula.has_key(arr[i][0]):
            oppose_formula[arr[i][0]].append(arr[i][1])
        else:
            oppose_formula[arr[i][0]] = [arr[i][1]]

        if oppose_formula.has_key(arr[i][1]):
            oppose_formula[arr[i][1]].append(arr[i][0])
        else:
            oppose_formula[arr[i][1]] = [arr[i][0]]

    N = int(arr[1 + C + 1 + D])
    spell = arr[-1]
    li = []
    for x in spell:
        if len(li) == 0:
            li.append(x)
        elif combine_formula.has_key((x, li[-1])):
            y = li.pop()
            li.append( combine_formula[(x, y)] )
        elif oppose_formula.has_key(x) and oppose_formula[x]:
            e = False
            for i in li:
                if i in oppose_formula[x]:
                    li = []
                    e = True
                    break
            if not e:
                li.append(x)
        else:
            li.append(x)
    
    output = '['
    for i in range(len(li)):
        if i == 0:
            output = output + li[i]
        else:
            output = output + ", " + li[i]
    output = output + ']'
    return output

def main(argv=None):
    if argv is None:
        argv = sys.argv
    if not len(argv) == 2:
        print >>sys.stderr, "Usage: store-credit.py infile"

    infile = argv[1]
    f = open(infile, 'r')
    N = int(f.readline())

    for i in range(N):
        line = f.readline().strip()
        result = magicka(line)
        print "Case #%d: %s" % (i + 1, result)
        
if __name__ == "__main__":
    sys.exit(main())
