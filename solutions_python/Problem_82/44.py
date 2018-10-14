for t in xrange(int(raw_input())):
    C,D=map(int,raw_input().split())
    points=[]
    for i in xrange(C):
        points.append(map(int,raw_input().split()))
    points.sort()
    groups=[]
    for i in points:
        g={}
        g['t']=((i[1]-1)/2.)*D
        g['l']=i[0]-((i[1]-1)*D/2.)
        g['r']=i[0]+((i[1]-1)*D/2.)
        groups.append(g)
    i=0
    while i <len(groups)-1:
       # print groups
        if (groups[i]['r']-groups[i+1]['l']>-D):
            #print "Group",i,"from",groups[i]['l'],"to",groups[i]['r'],"in",groups[i]['t'],"seconds."
            #print "Group",i+1,"from",groups[i+1]['l'],"to",groups[i+1]['r'],"in",groups[i+1]['t'],"seconds."
            overlap=groups[i]['r']-groups[i+1]['l']+D
            #Shift the idle group away
            if groups[i]['t']<groups[i+1]['t']:
                shift=min(groups[i+1]['t']-groups[i]['t'],overlap)
                groups[i]['l']-=shift
                groups[i]['r']-=shift
                groups[i]['t']+=shift
            else:
                shift=min(groups[i]['t']-groups[i+1]['t'],overlap)
                groups[i+1]['l']+=shift
                groups[i+1]['r']+=shift
                groups[i+1]['t']+=shift
            #Now that both groups take the same time to get to their positions
            #Shift them both away from each other
            #print groups
            shift=(groups[i]['r']-groups[i+1]['l']+D)/2.
            #print "shift",shift
            g={}
            g['t']=max(groups[i]['t'],groups[i+1]['t'])+shift
            g['l']=groups[i]['l']-shift
            g['r']=groups[i+1]['r']+shift
            groups[i:i+2]=[g]
            i-=2
        i=max(0,i+1)
   # print groups
    maxi=groups[0]['t']
    for i in groups:
        maxi=max(maxi,i['t'])
    print "Case #"+str(t+1)+":",maxi
