execfile('utils.py')


def process(fn):
    cases = [x.strip() for x in read1(fn)[1:]]
    res = [processCase(x) for x in cases]
    write2(fn+".out",res)

def processCase(case):
    scase = set(case)
    base = len(scase)
    lencase = len(case)
    res = 0

    if base == 1:
        base = 2

    digitsOrder = [1,0]+range(2,base)
    digitsIndex = 0
    T = {}
    for i in range(lencase):
        if case[i] not in T:
            T[case[i]] = digitsOrder[digitsIndex]
            digitsIndex += 1
        res *= base
        res += T[case[i]]

    return str(res)
