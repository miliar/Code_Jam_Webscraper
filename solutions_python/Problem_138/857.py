import sys
fin = open("D-large.in","r")
fout = open("war_output","w")
inp = fin.readline
out = fout.write
#out = sys.stdout.write

t = int(inp())
for case in xrange(1,t+1):
    n = int(inp())
    a = map(float,inp().split())
    b = map(float,inp().split())
    c = []
    d = []
    for e in a:
        c.append(e)
    for e in b:
        d.append(e) 

    #war:
    war_score = 0
    while len(c) > 0:
        opt = 100
        opt_i = 0
        for i in xrange(len(d)):
            if d[i] > c[0] and opt > d[i]:
                opt = d[i]
                opt_i = i
        if opt == 100:
            for i in xrange(len(d)):
                if d[i] < opt:
                    opt = d[i]
                    opt_i = i
            war_score+=1
        '''
        print c,c[0]
        print d,d[opt_i]
        if c[0]>d[opt_i]:
            print "Naomi wins"
        else:
            print "Kim wins"
        '''
        del d[opt_i]
        del c[0]


    #decietful-war
    a.sort()
    b.sort()
    dwar_score = 0
    while len(a)>0:
        if a[0] < b[0]:
            del a[0]
            del b[-1]
        else:
            del a[0]
            del b[0]
            dwar_score+=1
    
    out("Case #"+str(case)+": "+str(dwar_score)+" "+str(war_score)+"\n")

fin.close()
fout.close()
