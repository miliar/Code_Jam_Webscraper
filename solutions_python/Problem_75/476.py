#!/usr/bin/env python
# Google CodeJam Assignment B

def magickaQualify(*args):
    combine, delete, magic = args
    cDict = {}
    for c in combine:
        tSort = sort(c[:2])
        cDict[tSort] = c[-1]

    dDict = {}
    for d in delete:
        tSort = sorted(d)

        tGet = dDict.get(tSort[0], [])
        tGet.append(tSort[1])
        dDict[tSort[0]] = tGet

        tGet = dDict.get(tSort[1], [])
        tGet.append(tSort[0])
        dDict[tSort[1]] = tGet

    
    magicka = []
    for m in magic:
        if not magicka:
            magicka = [m]
            continue

        lastMagic = sort([m, magicka[-1]])
        if lastMagic in cDict:
            magicka[-1] = cDict[lastMagic]
        else:
            magicka.append(m)
            tempD = dDict.get(m, [])
            for contraMagic in tempD:
                if contraMagic in magicka[:-1]:
                    magicka = []
                    break

    return '[%s]' % ', '.join(m for m in magicka)


def sort(s):
    return ''.join(sorted(s))

def parseInput(line):
    commandList = line.split()
    magic = commandList.pop()
    N = int(commandList.pop())
    
    C = int(commandList.pop(0))
    combine = commandList[:C]

    commandList = commandList[C:]
    D = int(commandList.pop(0))
    delete = commandList[:D]

    assert(commandList[D:] == [])
    assert(N == len(magic))

    #print combine, delete, magic
    return [combine, delete, magic]

    
if __name__ == "__main__":
    mainfn = magickaQualify

    import sys
    if len(sys.argv)==1:
        filename = 'test.in'
    else:
        filename = sys.argv[1]

    f = open(filename)
    line = f.readline()
    for case in range(int(line)):
        args = parseInput(f.readline())
        print "Case #%i: %s" % (case+1, mainfn(*args))
