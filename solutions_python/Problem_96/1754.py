import os
import fileinput
import math

def testItem(t=0):
    dm = divmod(t, 3)
    if t==0:
        res = (0,0)
    else:
        if dm[1] == 0:
            res = (dm[0],dm[0]+1)
        elif dm[1] == 1:
            res = (dm[0]+1,dm[0]+1)
        elif dm[1] == 2:
            res = (dm[0]+1,dm[0]+2)
    return res

def getCommSurp(p, ti):
    common = 0
    surprising = 0
    for t in ti:
        test = testItem(int(t))
        if test[0] >= p:
            common += 1
        elif test[1] >= p:
            surprising += 1
    return (common, surprising)

if __name__ == '__main__':
    r = []
    filename = None

    for test in fileinput.input():
        if fileinput.isfirstline():
            filename = fileinput.filename()
        else:
            summ = 0
            items = test.split()
            s = int(items[1])
            p = int(items[2])
            ti = items[3:]

            res = getCommSurp(p, ti)
            summ = res[0] + min(res[1], s)

            prstr = 'Case #%d: %d%s' % (fileinput.lineno()-1, summ, "\n")
            r.append(prstr)
            print prstr

    if filename:
        f = open(os.path.join(os.path.dirname(filename), 'b-large.out'), 'w')
        f.writelines(r)
