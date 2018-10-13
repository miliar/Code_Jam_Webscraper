def small(line):
    va = 'nroygbv'
    n = line[0]
    sm = sum(line[1:])
    mx = max(line[1:])
    if(mx > (sm-mx)):
        return "IMPOSSIBLE"
    st = list()
    for i in range(1,len(va)):
        st.append((va[i], line[i]))
    st = sorted(st, key=lambda w: -w[1])
    ans = (st[0][0]+st[1][0]+st[2][0]) * max(0, sm - mx*2) + (st[0][0]+st[1][0]) * (st[1][1]-(sm-mx*2)) + (st[0][0]+st[2][0]) * (st[2][1]-(sm-mx*2))
    return ans
        

tt = int(input())
for case in range(1, tt+1):
    line = list(map(int, input().split()))
    print("Case #%d: %s"%(case, small(line).upper()))
