
f = open("C:\\Users\\TocarIP\\Google Drive\\Downloads\\C-large.in")
lines = f.readlines()
numcases = int(lines[0])
i = 1
while i <= numcases:
    n,k = [int(x) for x in lines[i].split()]
    res = "Case #" + str(i) + ": "
    mx = 0
    mn = 0
    to_solve = []
    to_solve.append((n,1))
    while k > 0:
        #print(to_solve)
        cur = to_solve[0]
        for x in to_solve[1:]:
            if x[0] > cur[0]: # min heap is for suckers
                cur = x

        #print(to_solve)
        to_solve.remove(cur)
        cnt = cur[1]
        if  k < cnt:
            to_solve.append((cur[0],cur[1]-k))
            cnt = k



        k -= cur[1]
        ls = cur[0]//2
        if cur[0] %2 == 0:
            ls -= 1
        ll = (ls,cnt)
        rr = (cur[0]//2,cnt)
        mx = max(ll[0],rr[0])
        if mx < 0:
            mx = 0
        mn = min(ll[0],rr[0])
        if mn < 0:
            mn = 0
        if ll[0] > 0:
            flag = True
            for x in to_solve:
                if x[0] == ll[0]:
                    to_solve.remove(x)
                    to_solve.append((x[0],x[1]+ll[1]))
                    flag = False
                    break
            if flag:
                to_solve.append(ll)
        if rr[0] > 0: #func decomposition stinks!!
            flag = True
            for x in to_solve:
                if x[0] == rr[0]:
                    to_solve.remove(x)
                    to_solve.append((x[0], x[1] + rr[1]))
                    flag = False
                    break
            if flag:
                to_solve.append(rr)
        #print(to_solve)

    print (res + str(mx) + " " + str(mn))
    i = i+ 1