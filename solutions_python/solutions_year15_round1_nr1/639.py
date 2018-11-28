

#Min eaten
def a(l):
    tot = 0
    for i in range(0,len(l)-1):
        if l[i+1] < l[i]:
            tot += l[i] - l[i+1]
    return tot



#min eaten assuming constant rate
def b(l):
    max_diff = max([float(l[i] - l[i+1]) for i in range(0,len(l)-1)])
    if max_diff <= 0:
        return 0

    tot = 0
    for i in range(0,len(l) - 1):
        tot += min(l[i],max_diff)
        

    return tot
    



t = int(raw_input())

for i in range(0,t):
    N = int(raw_input())
    m = map(int,raw_input().split(" "))

    

    print "Case #%d: %d %d" %(i+1,a(m),b(m))
