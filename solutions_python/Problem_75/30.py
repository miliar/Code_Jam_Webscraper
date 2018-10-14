


def addElement(lst, combines, oppositions, elem):
    combined = False
    destroyed = False
    if len(lst) >= 1:
        if (elem, lst[-1]) in combines:
            lst[-1] = combines[(elem, lst[-1])]
            combined = True
        if not combined and elem in oppositions:
            opps = oppositions[elem]
            for other in lst:
                if other in opps:
                    lst[:] = []
                    destroyed = True
                    break
    if not combined and not destroyed:
        lst.append(elem)
        
def main():
    testFile = open("test.txt")
    numCases = int(testFile.readline())
    for i in range(numCases):
        line = testFile.readline()[:-1].split(' ')
        c = int(line[0])
        combines = {}
        for j in range(c):
            triple = line[j + 1]
            combines[(triple[0], triple[1])] = triple[2]
            combines[(triple[1], triple[0])] = triple[2]
        d = int(line[1 + c])
        oppositions = {}
        for j in range(d):
            double = line[2 + c + j]
            if not double[0] in oppositions:
                oppositions[double[0]] = set([])
            oppositions[double[0]].add(double[1])
            if not double[1] in oppositions:
                oppositions[double[1]] = set([])
            oppositions[double[1]].add(double[0])
        elems = []
        for elem in line[-1]:
            addElement(elems, combines, oppositions, elem)
        print("Case #%d: [%s]" % (i + 1, ", ".join(elems)))

main()
        
        
