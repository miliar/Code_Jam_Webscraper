import time
s = time.time()
tidy_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
for i in range(10-1):
    new = []
    for j in range(i, 10-1):
        new.append((i+1)*10+tidy_list[0][j])
    tidy_list.append(new)

# 10 ** 2
tidy_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9]]
for i in range(10-1):
    new = []
    for j in range(i, 10-1):
        new.append((i+1)*10+tidy_list[0][j])
    tidy_list.append(new)

for m in range(16):
    #print m
    p = len(tidy_list)
    for i in range(1, 10):
        new = []
        for j in range(i+m*10-m, p):
            for k in range(len(tidy_list[j])):
                new.append(i*(10**(m+2))+tidy_list[j][k])
        tidy_list.append(new)
##print sum(map(len, tidy_list))
##print time.time()-s



#z = [99999999999999998]*100

ranges = [(1, 10, 0)]
idx = 1
for i in range(1, 19):
    for j in range(1, 10):
        ranges.append(((10**i)*j+1, (10**i)*(j+1), idx))
        idx += 1
##print ranges
##print idx
for c in range(1, int(raw_input())+1):
    q = int(raw_input())
    index = -1
    for i in range(len(ranges)):
        if q >= ranges[i][0] and q <= ranges[i][1]:
            #print ranges[i]
            index = ranges[i][2]
    #print "index", index

    ans = -1
    if tidy_list[index][0] <= q:
        for i in range(len(tidy_list[index])):
            if tidy_list[index][i] == q:
                ans = tidy_list[index][i]
                break
            elif tidy_list[index][i] > q:
                if i > 1:
                    #print i
                    ans = tidy_list[index][i-1]
                    break
        if ans == -1:
            ans = tidy_list[index][0]
    else:
        ans = tidy_list[index-1][len(tidy_list[index-1])-1]
    print "Case #{}: {}".format(c, ans)
##print time.time()-s

        


