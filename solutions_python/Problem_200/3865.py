import fileinput
f = fileinput.input()
t = input()
c = 0
while c<t:
    c += 1
    n = input()
    res = 0
    maxdiff = n

    def dfs(x):
        global res, maxdiff
        #print x, n-int(x), maxdiff
        if int(x)<=n and n-(int(x)) <= maxdiff:
            res = x
            maxdiff = n-(int(x))
        
        if int(x)>n:
            return
        
        i = int(x[0])
        while i>0:
            #print "in"
            dfs(str(i)+x)
            i -= 1
    i = 9
    while i>0:
        dfs(str(i))
        i-=1
    print "Case #"+str(c)+": "+str(res)

