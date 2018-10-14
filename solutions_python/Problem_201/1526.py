import heapq

f = open("C-small-2-attempt4.in.txt")
out = open("output.txt", "w")
di = {}
di[999999] = 524287
di[1000000] = 524287
di[500000] = 262143
t = int(f.readline().strip())
tt = 1
res = []
while tt <= t:
    n, k = map(int, f.readline().strip().split())
    if n in di and k >= di[n]:
        if k > di[n]:
            #out.write("Case #" + str(tt) + ": 0 0\n")
            res.append("Case #" + str(tt) + ": 0 0")
        else:
            #out.write("Case #" + str(tt) + ": 1 0\n")
            res.append("Case #" + str(tt) + ": 1 0")
    else:
        h = []
        heapq.heappush(h, -n)
        while k-1 > 0:
            elem = -heapq.heappop(h)
            nn = elem/2
            if elem % 2 == 0:
                heapq.heappush(h, -nn)
                heapq.heappush(h, -(nn - 1))
            else:
                heapq.heappush(h, -nn)
                heapq.heappush(h, -nn)
            k -= 1
        ans = -heapq.heappop(h)
        a2 = a1 = ans/2
        if ans % 2 == 0:
            a2 -= 1
        #out.write("Case #" + str(tt) + ": " + str(a1) + " " + str(a2) + "\n")
        res.append("Case #" + str(tt) + ": " + str(a1) + " " + str(a2))
    tt += 1

out.write("\n".join(res))
