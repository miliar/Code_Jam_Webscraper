
def WP(data):
    wins=data.count("1")
    lost=data.count("0")
    return float(wins)/(lost+wins)

def OWP(games, data, pos):
    count=0
    wps=[]
    for i in xrange(0,len(games)):
        if games[i] in "01" and i!=pos:
            d=list(data[i])
            d[pos]="."
            d="".join(d)
            wps.append(WP(d))
            count+=1
    return sum(wps)/count

def OOWP(games, data, pos):
    count=0
    owps=[]
    for i in xrange(0, len(games)):
        if games[i] in "01" and i!=pos:
            owps.append(OWP(data[i],data, i))
            count+=1
    return sum(owps)/count

def RPI(games, data, pos):
    return 0.25*WP(games) + 0.5*OWP(games, data, pos) + 0.25*OOWP(games, data, pos)

def checkCase(caseData):
    return 0


data=open("A-large.in","r").read()


data=data.splitlines()[1:]
data.reverse()
out=open("out.txt","w")
c=0
while data:
    c+=1
    t_count=int(data.pop())
    teams=[]
    games=0
    for i in xrange(0,t_count):
        t=data.pop()
        games=len(t)
        teams.append(t)
    out.write("Case #%i:\n"%c)
    for i in xrange(0, t_count):
        out.write(str(RPI(teams[i],teams, i)))
        out.write("\n")
    out.flush()
    
out.close()
