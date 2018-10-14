from math import pi

fil = open("A.in")
out = open("A.txt", "w")

input = fil.readline
print = out.write

def func(N, K, pan):
    max_ar = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if pan[i][0] < pan[j][0]:
                pan[i], pan[j] = pan[j], pan[i]
            elif pan[i][0] == pan[j][0] and pan[i][1] < pan[j][1]:
                pan[i], pan[j] = pan[j], pan[i]
    for i in range(N):
        area = pan[i][0]**2 * pi
        area += 2*pi*pan[i][0]*pan[i][1]
        if K == 1:
            max_ar = max(max_ar, area)
            continue
        for j in range(i+1, N):
            ar2 = area + 2*pi*pan[j][0]*pan[j][1]
            if K == 2:
                max_ar = max(max_ar, ar2)
                continue
            for k in range(j+1, N):
                ar3 = ar2 + 2*pi*pan[k][0]*pan[k][1]
                if K == 3:
                    max_ar = max(max_ar, ar3)
                    continue
                for l in range(k+1, N):
                    ar4 = ar3 + 2*pi*pan[l][0]*pan[l][1]
                    if K == 4:
                        max_ar = max(max_ar, ar4)
                        continue
                    for m in range(l+1, N):
                        ar5 = ar4 + 2*pi*pan[m][0]*pan[m][1]
                        if K == 5:
                            max_ar = max(max_ar, ar5)
                            continue
                        for n in range(m+1, N):
                            ar6  = ar5 + 2*pi*pan[n][0]*pan[n][1]
                            if K == 6:
                                max_ar = max(max_ar, ar6)
                                continue
                            for o in range(n+1, N):
                                ar7 =ar6+ 2*pi*pan[o][0]*pan[o][1]
                                if K == 7:
                                    max_ar = max(max_ar, ar7)
                                    continue
                                for p in range(o+1, N):
                                    ar8 =ar7+ 2*pi*pan[p][0]*pan[p][1]
                                    if K == 8:
                                        max_ar = max(max_ar, ar8)
                                        continue
                                    for q in range(p+1, N):
                                        ar9 =ar8+ 2*pi*pan[q][0]*pan[q][1]
                                        if K == 9:
                                            max_ar = max(max_ar, ar9)
                                            continue
                                        for r in range(q+1, N):
                                            ar10 =ar9+ 2*pi*pan[r][0]*pan[r][1]
                                            if K == 10:
                                                max_ar = max(max_ar, ar10)
                                                continue
    return max_ar
                                    


for t in range(int(input())):
    N, K = map(int, input().split(' '))
    pan = [list(map(int, input().split(' '))) for i in range(N)]
    ans = func(N, K, pan)
    print("Case #{}: {}\n".format(t+1, ans))
