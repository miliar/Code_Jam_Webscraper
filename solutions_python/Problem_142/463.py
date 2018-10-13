import itertools
import operator
TotalCases = 0

def checkIfPossible(strings):
    prev = ''
    for foo in strings:
        fo = ''.join(ch for ch, _ in itertools.groupby(foo))
        if prev != '':
            if prev != fo:
                return False
        prev = fo
    return True

def expand(str,i):
    l = list(str)
    l.insert(i,str[i])
    return ''.join(l)

def contract(str,i):
    l = list(str)
    del l[i]
    return ''.join(l)

def doWork(str,i):
    if i == 0:
        return expand(str,i)
    else:
        if str[i-1] == str[i]:
            return contract(str,i-1)
        else:
            return expand(str,i-1)


def pickDiff(l):
    cd = {}
    for c in l:
        if not cd.has_key(c):
            cd[c] = 1
        else:
            cd[c] = cd[c]+1
    oddone = min(cd.iteritems(), key=operator.itemgetter(1))[0]
    return l.index(oddone)

def addTrail(l):
    size = len(max(l, key=len))
    for i in range(len(l)):
        l[i] = l[i].ljust(size)
    return l

def solveCase(testNumber):
    testNumber = testNumber+1
    StringsCount = int(raw_input())
    strings = []
    for s in range(StringsCount):
        strings.append(raw_input())
    if not checkIfPossible(strings):
        print "Case #"+str(testNumber)+": Fegla Won"
        return
    strings = addTrail(strings)
    done = False
    i = 0
    moves = 0
    while i < len(strings[0]):
        chars = []
        for s in strings:
            chars.append(s[i])
        if all(chars[0] == item for item in chars):
            i = i+1
        else:
            odd = pickDiff(chars)
            f = doWork(strings[odd],i)
            strings[odd] = f
            strings = addTrail(strings)
            moves = moves+ 1
    print "Case #"+str(testNumber)+": "+str(moves) 


def main():
    TotalCases = raw_input()
    TotalCases = int(TotalCases)
    for testCase in range (TotalCases):
        solveCase(testCase)

if __name__ == "__main__":
    main()
