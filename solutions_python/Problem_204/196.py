ncase = int(input())

from math import floor

def cal(per, val):
    # cal per and val and ratio
    begin = floor(val / per)
    s = []
    # print(begin, floor(begin * 0.8 - 5), floor(begin * 1.2 + 5))
    if val> 0.85 * per:
        if per < 100:
            begin, end = floor(begin * 0.8 - 15), floor(begin * 1.2 + 15)
        else:
            begin, end = floor(begin * 0.88 - 2), floor(begin * 1.12 + 2)
        for i in range(begin, end):
            if val >= 0.9 * i * per and val <= 1.1 * i * per:
                s.append(i)
    # print(s)
    return s


for case in range(1, ncase+1):
    np = [int(s) for s in input().split(" ")]
    n = np[0]
    p = np[1]
    ri = [int(s) for s in input().split(" ")]
    qij = []
    for i in range(n):
        s = [int(s) for s in input().split(" ")]
        qij.append(sorted(s))

    # print(ri, qij)
    n_serves = 0
    indexes = [0] * n

    def update_index():
        mins = []
        for i in range(n):
            # print(ri[i], qij[i][0])
            j = indexes[i]
            s = []
            while len(s) == 0 and j < p:
                s = cal(ri[i], qij[i][j])
                j += 1
            indexes[i] = j
            mins.append(s)
        return mins

    mins = update_index()
    # print(indexes)
    # print(mins)

    minmax = 0
    iminmax = 0
    maxmin = 5000000
    imaxmin = 0


    flag = True
    while 1:
        changes = True
        minmax = 0
        iminmax = 0
        maxmin = 5000000
        imaxmin = 0
        for i in range(n):
            s = mins[i]
            if len(s) == 0:
                changes = False
                break
            if s[0] > minmax:
                minmax = s[0]
                iminmax = i
            if s[-1] < maxmin:
                maxmin = s[-1]
                imaxmin = i
        if changes == False:
            break
        # print("mins", mins)
        # print("mm", minmax, maxmin, changes)
        if minmax <= maxmin:
            # able to serve
            n_serves += 1
            # print(mins)
            mins = update_index()
            # print(mins)
            continue
        else:
            # imaxmin update
            # print("up single, {}".format(imaxmin))
            s = []
            j = indexes[imaxmin]
            # print("j", j)
            while len(s) == 0 and j < p:
                # print(ri[imaxmin], qij[imaxmin][j])
                s = cal(ri[imaxmin], qij[imaxmin][j])
                j += 1
            # print(j)
            indexes[imaxmin] = j
            # print(s)
            if j == p and len(s) == 0:
                break
            if j==p and max(s) < minmax:
                # print("hello")
                break
            indexes[imaxmin] = j
            mins[imaxmin] = s
            # print("s", s)
            # print(mins)







    print("Case #{}: {}".format(case, n_serves))



