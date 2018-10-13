def tidy(n):
    if n < 10:
        return n
    flag = False
    ln = [int(x) for x in str(n)]
    while flag == False:
        for c in range(1, len(ln)):
            if ln[c] < ln[c-1]:
                ln[c-1] -= 1
                for z in range(c, len(ln)):
                    ln[z] = 9
                break
            elif c == len(ln) - 1:
                flag = True

    sn = [str(x) for x in ln]
    return int("".join(sn))

    # for i in range(n, 0, -1):
    #     ln = [int(x) for x in str(i)]
    #     t = True
    #     for c in range(1, len(ln)):
    #         if ln[c] < ln[c-1]:
    #             t = False
    #             break
    #     print(i)
    #     if t == True:
    #         return i

t = int(input())

for i in range(1, t+1):
    n = int(input())
    print("Case #{}: {}".format(i, tidy(n)))
