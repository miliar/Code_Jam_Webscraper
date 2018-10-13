



def can_reach(x, v, B, T):
    y = x + v*T
    if y>=B:
        return '1'
    return '0'
    
    
input = open("e:/B-large.in", "r")
for testcase in range(1, int(input.readline())+1):
    N,K,B,T = map(int, input.readline().split(' '))
    x = map(int, input.readline().split(' '))
    v = map(int, input.readline().split(' '))
    c = "".join(can_reach(x[i], v[i], B, T) for i in range(N))
    if sum(int(a) for a in c)<K:
        print "Case #%d: IMPOSSIBLE"%testcase
        continue
        
    #print c
    ans=0
    target = "1"*K
    while not c.endswith(target):
        i = c.rindex("10") #i then j
        j = c.rindex("0")
        #print c, "switching", i, j, "cost=", (j-i)
        c = c[:i]+'0'+c[i+1:j]+'1'+c[j+1:]
        #print c
        ans+=j-i
        
    
    print "Case #%d:"%testcase, ans


