__author__ = 'cdong'


def getSet(fin):
    a = int(fin.readline()) - 1
    ret = set()
    for i in range(4):
        l = fin.readline()
        if (i == a):
            ret.update(l.split())
    return ret


def solve(test, fin):
    a1 = getSet(fin)
    a2 = getSet(fin)
    a = a1 & a2
    # answer = 0
    if (len(a) == 0):
        answer = 'Volunteer cheated!'
    elif (len(a) > 1):
        answer = 'Bad magician!'
    else:
        answer = next(iter(a))
    print("Case #%d:" % test, answer)

fin = open('input.txt')
# fin = open('/Users/cdong/Downloads/A-small-attempt0.in.txt')
noTests = int(fin.readline())
for i in range(noTests):
    solve(i + 1, fin)

