import sys
import itertools

def war(naomi,ken):
    naomi.sort()
    ken.sort()
    res = 0
    while len(naomi) > 0:
        #x = naomi[0]
        x = naomi.pop(0)
        tmp = filter(lambda y:y>x,ken)
        if len(tmp) == 0:
            kenChoice = min(ken)
        else:
            kenChoice = min(tmp)
        # ken = ken - {kenChoice}
        # naomi = naomi - {x}
        if x > kenChoice:
            res = res + 1
        #naomi = naomi[1:]
        for index,y in enumerate(ken):
            if y == kenChoice:
                ken.pop(index)
                break
    return res


def deceitfulWar(naomi, ken):
    naomi.sort()
    ken.sort()
    ken = [x for x in reversed(ken)]
    res = 0
    while len(naomi) > 0:
        x = naomi.pop(0)
        tmp = filter(lambda y: y < x,ken)
        if len(tmp) == 0:
            kenChoice = max(ken)
        else:
            kenChoice = max(tmp)
            res = res + 1
        for index,y in enumerate(ken):
            if y == kenChoice:
                ken.pop(index)
                break
    return res
    #return len(filter(lambda x: len(filter (lambda y:y<x,ken)),naomi))

def parse(inputStr):
    return map(float, inputStr.split(" "))

def main():
    fileName = sys.argv[1]
    f = open(fileName, 'r+')
    lines = [line for line in f]
    nCases = int(lines[0])
    lines = lines[1:]
    k = 1
    while k <= nCases:
        tmp = lines[0]
        naomiStr = lines[1]
        kenStr = lines[2]
        deceit = deceitfulWar(parse(naomiStr),parse(kenStr))
        honest = war(parse(naomiStr),parse(kenStr))
        print "Case #"+str(k)+": "+str(deceit)+ " "+str(honest)
        k = k+1
        lines  = lines[3:]

if __name__ == "__main__":
    main()

