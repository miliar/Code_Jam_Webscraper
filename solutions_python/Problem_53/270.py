def get_res(s,n):
    m = n
    for i in range(0,s):
        if(m%2==0):
            return "OFF"
        m = m/2
    if n==0:
        return "OFF"
    return "ON"
f = open("A-large.in","r")
count = 0
for l in f:
    if count!=0:
        d = l.split(" ")
        print "Case #%d: %s" %(count,get_res(int(d[0]),int(d[1])),)
    count = count + 1
f.close()
