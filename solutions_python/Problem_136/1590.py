#!/usr/bin/python

baseProd = 2

def main():
    fin = open('B-large.in', 'r')
    fout = open('cookie.out', 'w')

    fin.seek(0)
    ncases = int(fin.readline())
    for i in range(1, ncases + 1):
        cost, prod, win = [float(i) for i in fin.readline().strip().split()]
        calcTimeMemo = [0]
        prevTime = win / baseProd
        curTime = cost / baseProd + win / (baseProd + prod)
        nFarms = 1
        while curTime < prevTime:
            nFarms += 1
            prevTime = curTime
            curTime = calcTime(cost, prod, nFarms) + win / (baseProd + prod * nFarms)
        fout.write("Case #{0}: {1:.7f}".format(i, prevTime) + "\n")

calcTimeMemo = {}
def calcTime(cost, prod, num):
    if (cost, prod, num) in calcTimeMemo:
        return calcTimeMemo[(cost, prod, num)]
    elif num < 1:
        return 0
    else:
        totTime = (cost / (baseProd + (num - 1) * prod) +
          calcTime(cost, prod, num - 1))
        calcTimeMemo[(cost, prod, num)] = totTime
        return totTime


if __name__ == "__main__":
    main()
