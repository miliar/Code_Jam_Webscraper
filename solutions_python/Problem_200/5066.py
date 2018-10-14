t=int(raw_input())
for i in range(t):
    n=int(raw_input())
    for j in range(n,0,-1):
        s=str(j)
        while True:
            if len(s)<4:
                s="0"+s
            else:
                break
        if s[0]<=s[1] and s[1]<=s[2] and s[2]<=s[3]:
            print "Case #"+str(i+1)+": "+str(int(s))
            break
