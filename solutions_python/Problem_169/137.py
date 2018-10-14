
test = int(input())

for t in range(1, test+1):
    print("Case #" + str(t) + ": ", end="")
    line1 = input().split(' ')
    N = int(line1[0])
    tV = float(line1[1])
    tT = float(line1[2])
    if N == 1:
        line2 = input().split(' ')
        r = float(line2[0])
        t = float(line2[1])
        if t != tT:
            print('IMPOSSIBLE')
        else:
            print(tV / r)
    elif N == 2:
        line2 = input().split(' ')
        line3 = input().split(' ')
        r1 = float(line2[0])
        t1 = float(line2[1])
        r2 = float(line3[0])
        t2 = float(line3[1])
        if t1 > t2:
            t1, t2 = t2, t1
            r1, r2 = r2, r1
        if t1 == t2 == tT:
            print(tV / (r1+r2))
        elif t1 <= tT <= t2:
            x = (tT - t2) / (t1 - t2) * tV
            time1 = x / r1
            time2 = (tV - x) / r2
            print(max(time1, time2))
        else:
            print('IMPOSSIBLE')



