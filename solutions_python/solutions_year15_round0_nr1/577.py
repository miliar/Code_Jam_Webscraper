s = open("in")
n2 = int(s.readline().strip())

o = open("out","w")
for i in range(1,n2+1):
    n,p = s.readline().strip().split()
    n = int(n)
    ans = 0
    total = 0
    for j in range(n+1):
        if total < j:
            ans += j-total
            total = j
        total += int(p[j])
    o.write("Case #"+str(i)+": "+str(ans)+"\n")
