f = open("inp3", "r")
t = int(f.readline())
for tt in range(1,t+1):
    a,b = map(int, f.readline().split())
    c = 0
    for n in range(a,b):
        nn = len(str(n))
        mm = list()
        s = str(n)+str(n)
        for i in range(nn):
            m = int(s[i:i+nn])
            if m>n and m<=b and m not in mm:
                c+=1; mm.append(m)
    print "Case #"+str(tt)+":",c
