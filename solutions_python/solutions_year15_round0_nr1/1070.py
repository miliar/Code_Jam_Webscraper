


t = int(raw_input())

for i in range(0,t):
    s = raw_input()
    smax = int(s.split(" ")[0])

    n = 0
    count = 0
    l = s.split(" ")[1]

    for j in range(0,smax+1):
        if j > count + n:
            n += j - (count + n)
        count += int(l[j])
        

    print "Case #%d: %d" %(i+1,n)
