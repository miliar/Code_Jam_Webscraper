import sys
import math

filein = sys.argv[1]
freader = open(filein, 'r').read().splitlines()
case = 0
#test_cases = int(freader[0])

# runs all test cases
for rowf in freader[1:]:
    case=case + 1
    dic_combine=dict()
    dic_opposed=dict()
    data=rowf.split(' ')[0:]
    c=int(data[0])
    if (c > 0):
        cstrs=data[1:1+c]
        for el in cstrs:
            dic_combine[''.join(sorted(el[0:2]))] = el[2:3]
    d=int(data[1 + c])
    if (d > 0):
        dstrs = data[2+c:1+c+d+1]
        for el in dstrs:
            dic_opposed[''.join(sorted(el[0:2]))] = ""
    e=data[-1]

    result=""
    for el in e:
        combine=el
        changed=False
        if (len(result) > 0):
            k=''.join(sorted(combine + result[-1]))
            if k in dic_combine:
                result=result[:-1]+dic_combine[k]
                changed=True
                combine=dic_combine[k]

            # check for opposed
            toCheck=result
            if (changed):
                toCheck=result[:-1]
            for er in toCheck:
                k=''.join(sorted(combine + er))
                if k in dic_opposed:
                    result=""
                    break
            if result != "" and not changed:
                result=result+combine
        else:
            result=combine
    print 'Case #%d: [%s]' % (case, ', '.join(list(result)))
