import math

t = int(input())

for c in range(t):
    A,B = map(int,input().split())
    timeA = 720
    timeB = 720
    vals = []
    for i in range(A):
        b,e = map(int,input().split())
        timeA -= e-b
        vals.append(("a",b,e))
    for i in range(B):
        b,e = map(int,input().split())
        timeB -= e-b
        vals.append(("b",b,e))
    times = []
    curP = -1
    val = []
    for v in sorted(vals,key = lambda x:x[1]):
        if v[0] == curP:
            val.append(v)
        else:
            curP = v[0]
            if val:
                times.append(val)
            val = [v]
#     print(vals)
    if times :
        if val[0][0] == times[0][0][0]:
            for v in val:
                times[0].append((v[0],v[1]-1440,v[2]-1440))
        else:
            times.append(val)
        intervals = []
        for val in times:
            if len(val) > 1:
                val = sorted(val, key = lambda x:x[1])
                v1 = val[0]
                for v in val[1:]:
                    interval = v[1] - v1[2]
                    intervals.append((interval,v[0]))
                    v1 = v
        still = []
        for inte in sorted(intervals):
            if inte[1] == 'a' and inte[0] <= timeA:
                timeA -= inte[0]
                continue
            if inte[1] == 'b' and inte[0] <= timeB:
                timeB -= inte[0]
                continue
            still.append(inte)

        minChange = len(times)
        total = minChange + 2*len(still)
        print("Case #%s: %d"%(c+1,total))
    elif len(val) >= 2:
        val = sorted(val, key = lambda x:x[1])
        intervals = [(val[0][1] - val[-1][2])+1440]
        v1 = val[0]
        for v in val[1:]:
            interval = v[1] - v1[2]
            intervals.append(interval)
            v1 = v
        still = []
        time = min(timeA,timeB)
        for inte in sorted(intervals):
            if  inte <= time:
                timeA -= inte
                continue
            still.append(inte)
#         print(intervals,still)
        total = 2*len(still)
        print("Case #%s: %d"%(c+1,total))
    else:
        print("Case #%s: %d"%(c+1,2))






# pstr, k = input().split()
# k = int(k)
# size = len(pstr)
# pstr = [a == "+" for a in pstr]
# 
# i = 0
# flips = 0
# while i <= size-k:
# 	if not pstr[i]:
# 		flips += 1
# 		for j in range(i, i+k):
# 			pstr[j] = not pstr[j]
# 	i += 1
# 
# print("Case #%d: " % (c+1), end="")
# ok = True
# for x in range(size-k, size):
# 	if not pstr[x]:
# 		print("IMPOSSIBLE")
# 		ok = False
# 		break
# if ok:
# 	print(flips)

