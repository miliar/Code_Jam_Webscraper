def nma(num, p):
    # 1
    num = int(num)
    p = int(p)
    lst = [num]
    for k in range(p):
        # print(lst)
        temp = max(lst)
        # lst.remove(temp)
        lst.remove(temp)
        if temp % 2:
            res_f = temp // 2
            res_s = temp // 2
        else:
            res_f = temp / 2
            if res_f == 0:
                res_s = 0
            else:
                res_s = res_f - 1
        if res_f > 0:
            lst.append(res_f)
        if res_s > 0:
            lst.append(res_s)
    #print(lst, lst.count(1), lst.count(0))
    return int(res_f), int(res_s)
n = int(input())
res = ""
for i in range(n):
    res += "Case #{0}: {1} {2}\n".format(i+1, *nma(*input().strip().split(" ")))
print(res, end="")
