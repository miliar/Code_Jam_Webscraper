f = open('B-large.in','r')
inp = f.read().split('\n')
T = int(inp[0])
inp = inp[1:]
fi = open('2ans.txt','w')
for t in xrange(T):
    rate=2
    time,timeD=0,0
    total = 0
    d = inp[t].split(' ')
    c,f,x = float(d[0]),float(d[1]),float(d[2])
    while 1:
        timeC= c/(rate)
        timeD= x/(rate+f)
        timeT=timeD+timeC
        time = x/rate
        if time<timeT:
            total+=time
            break
        if (time-timeT < 10**(-10)):
            total+=time
            break
        total+=timeC
        rate+=f
    
    fi.write('Case #'+str(t+1)+': '+ "%.7f" % total)
    if t!=T-1:
        fi.write('\n')
fi.close()
    
