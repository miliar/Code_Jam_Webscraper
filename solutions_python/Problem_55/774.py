f = open ("C-small.in")
num = int(f.readline())
for z in range (1,num+1):
    t1 = f.readline().split()
    mx = int(t1[1])
    groups = f.readline().split()
    length = len(groups)
    for i,num in enumerate(groups):
        groups[i] = int(num)
    mon = 0
    for i in range (0,int(t1[0])):
        t = 0
        x = length
        back = []
        speed1 = groups.pop
        speed2 = back.append
        while x is not 0:
            t += groups[0]
            if t<mx:
                speed2(speed1(0))
                x-=1
            elif t == mx:
                speed2(speed1(0))
                x-=1
                break                
            elif t> mx:
                t -= groups[0]
                break
        groups += back
        back = []
        mon += t
    print "Case #"+str(z)+": "+str(mon)
