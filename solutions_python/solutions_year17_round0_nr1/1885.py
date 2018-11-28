def nma(num, p):
    # 0 1 2 3 4
    # print(num, p)
    num = list(num)
    count = 0
    p = int(p)
    for k in range(len(num)-p+1):
        if num[k] == "-":
            for jk in range(k, k+p):
                if num[jk] == "-":
                    num[jk] = "+"
                else:
                    num[jk] = "-"
            count += 1
        # print(num)
    for k in range(len(num)-p, len(num)):
        if num[k] == "-":
            count = "IMPOSSIBLE"
    return count
n = int(input())
res = ""
for i in range(n):
    res += "Case #{0}: {1}\n".format(i+1, nma(*input().strip().split(" ")))
print(res)
