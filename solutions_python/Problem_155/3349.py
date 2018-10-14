
f = open("A-large.in", 'r')
f2 = open("result2.txt", "w")
idx = 0
for l in f:
    if idx == 0:
        idx += 1
        continue
    val = map(int, [c for c in str.split(l)[1]])
    #print val
    s_max = len(val)
    res = 0
    up = 0
    for s in range(s_max):
        k = val[s]
        if up < s:
            res += (s-up)
            up += (s-up)
        up += k
        #print s, up, res
        #print up, res
    result =  "Case #" +str(idx)+": "+str(res)+ "\n"
    f2.write(result)
    idx += 1
