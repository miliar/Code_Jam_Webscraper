import sys

def get_owp(team, sch, n):
    suma = 0
    for i in range(0,n):        
        if sch[team][i] != '.':
            copy = []
            for c in sch[i]:
                copy.append(c)      
            if copy[team] != '.':
                copy[team] = '.'
            copy = "".join(copy)   
            suma = suma + copy.count("1")/(n-copy.count(".")*1.0)
    return suma/(n-sch[team].count("."))

def get_oowp(sch, team, owp, n):
    suma = 0
    for i in range(0,n):
        if sch[team][i] != '.':
            suma = suma + owp[i]          
    return suma/(n-sch[team].count("."))
                         

with open(sys.argv[1]) as f:
    t = (int)(f.readline())
    for i in range(0,t):
        n = (int)(f.readline())
        schedule = []
        wp = []
        owp = []
        oowp = []                 
        for j in range(0,n):
            schedule.append(f.readline())        
            wp.append(schedule[j].count("1")/((n-schedule[j].count("."))*1.0))
        for j in range(0,n):
            owp.append(get_owp(j,schedule,n))
        for j in range(0,n):
            oowp.append(get_oowp(schedule, j,owp,n))
        print "Case #"+str(i+1)+":"
        
        for j in range(0,n):                
            print 0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]
