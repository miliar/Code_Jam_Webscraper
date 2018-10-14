def nma(num):
    # 5 5 4
    # 5 4 9
    num = list((int(j) for j in num))
    for k in range(len(num)-1):
        if num[k] > num[k+1]:
            num[k] -= 1
            saved_v = k + 1
            num[k+1] = 9
            # for f in range(k+1, len(num)):
            #     num[f] = 9
            count = 0
            for np in range(k, -1, -1):
                if num[np] > num[np+1]:
                    # if np != k:
                    saved_v = np + 1
                    num[np]-=1
                else:
                    if count > 2:
                        break
                count += 1
            for jpp in range(saved_v, len(num)):
                num[jpp] = 9
            break
    return int("".join((str(jp) for jp in num)))

n = int(input())
res = ""
for i in range(n):
    res += "Case #{0}: {1}\n".format(i+1, nma(input().strip()))
print(res)
