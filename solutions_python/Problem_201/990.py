T = int(input())
for t in range(0,T):
    print("Case #{}: ".format(t+1), end='')
    n,k = [int(e) for e in input().split()]
    dic = {n:1}
    tg = -1
    while(k > 0):
        lst = list(dic.keys())
        lst.sort(reverse=True)
        for e in lst:
            cnt = dic.pop(e)
            k -= cnt
            if(k <= 0):
                tg = e
                break
            e -= 1
            dic[int(e/2)] = dic[int(e/2)]+cnt if int(e/2) in dic.keys() else cnt
            dic[int((e+1)/2)] = dic[int((e+1)/2)]+cnt if int((e+1)/2) in dic.keys() else cnt
    ret = [int(tg/2), int((tg-1)/2)]
    print("{} {}".format(max(ret), min(ret)))
