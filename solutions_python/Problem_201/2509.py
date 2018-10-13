def last_stall_values(n, k):
    mx = 0
    mn = 0
    stalls = [['o', (None, None)]]
    for i in xrange(0, n):
        stalls.append(['.', (None, None)])
    stalls.append(['o', (None, None)])
    for i in xrange(1, k+1):
        for j in xrange(1, len(stalls)-1):
            if stalls[j][0] == 'o':
                continue
            ls = 0
            for k in xrange(j-1,0,-1):
                if stalls[k][0] == '.':
                    ls += 1
                else:
                    break
            rs = 0
            for k in xrange(j+1,len(stalls)):
                if stalls[k][0] == '.':
                    rs += 1
                else:
                    break
            stalls[j][1] = (ls, rs)
        mins = [(i,min(l, r)) for i, (s, (l,r)) in enumerate(stalls) if s == '.']
        max_of_mins = max(mins, key=lambda (i, v): v)
        max_of_mins_list = [m for m in mins if m[1] == max_of_mins[1]]
        if(len(max_of_mins_list) == 1):
            stall_idx = max_of_mins[0]
        else:
            maxs = [(i,max(stalls[i][1])) for i, _ in max_of_mins_list]
            max_of_maxs = max(maxs, key=lambda (i, v): v)
            stall_idx = max_of_maxs[0]
        stalls[stall_idx][0] = 'o'
        mx = max(stalls[stall_idx][1])
        mn = min(stalls[stall_idx][1])
    return mx, mn

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n, k = [int(s) for s in raw_input().split(" ")]
    mx, mn = last_stall_values(n, k)
    print "Case #{}: {} {}".format(i, mx, mn)
