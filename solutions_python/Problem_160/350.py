def statusAtT(t, timeList):
    finished = 0
    leftTimeList = []
    for time in timeList:
        d, m = divmod(t, time)
        finished += int(d)
        if m == 0:
            leftTimeList.append(0)
        else:
            leftTimeList.append(time - m)
    return finished, leftTimeList

def approximateTime(N, timeList):
    return int( (max(N//len(timeList)-1, 0))*len(timeList) /sum([1/time for time in timeList]))

def solve(B, N, timeList):
    t = approximateTime(N, timeList)
##    print(t)
    while True:
        finished, leftTimeList = statusAtT(t, timeList)
        zeroCount = leftTimeList.count(0)
##        print(t, finished, leftTimeList, zeroCount)
        if finished + B - zeroCount < N <= finished + B:
            n = N - (finished + B - zeroCount)
            return [k+1 for k, leftTime in enumerate(leftTimeList) if leftTime==0][n-1]
        t += 1
    return 'error'

fin = open('B-small-attempt3.in')
caseNum = int(fin.readline())

for caseNo in range(caseNum):
    B, N = list(map(int, fin.readline().strip().split()))
    timeList = list(map(int, fin.readline().strip().split()))
##    print(N, timeList)
    print('Case #%d: %d' % (caseNo+1, solve(B, N, timeList)))
fin.close()
