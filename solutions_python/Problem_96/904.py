





def gogo(s,p,t):
    ret = 0
   # print "goal: ", p
    if p <= 0:
        return len(t)
    if p > 10:
        return 0
    for c in t:
        if c == 0 and p > 0:
            continue
        if c == 1 and p > 1:
            continue
        
        if c  >= 3*p - 2:
            #print c
            ret += 1
        elif c >= 3*p - 4 and s > 0:
            #print c, "Special"
            ret += 1
            s -= 1
            #print s
    return ret




s = open("c:/Users/Kevin Hulin/Downloads/B-large.in")
#s = open("c:/Users/Kevin Hulin/Downloads/Btest.in")

s = s.readlines()
for i in range(0,len(s)):
    s[i] = s[i].replace("\n","")



t = int(s[0])

f = open("c:/Users/Kevin Hulin/Downloads/Bsmall.out","w")



for i in range(1,t+1):
    v = s[i].split(" ")
    n = int(v[0])
    surprising = int(v[1])
    p = int(v[2])
    w = []
    for j in range(0,n):
        w.append(int(v[j+3]))
    f.write("Case #" + str(i) + ": " + str(gogo(surprising,p,w)))
    if i < t:
        f.write("\n")

f.close()



    
