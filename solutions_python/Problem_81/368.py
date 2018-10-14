import numpy as np
import sys



f = sys.stdin
t = int(f.readline())
for i in range(t):
    n = int(f.readline())
    winlose = np.zeros([n,n])
    plays = np.zeros([n,n])
    for j in range(n):
        l = f.readline()
        x=0
        for val in l[:-1]:
            if val=='1':
                winlose[j,x]=1
            if val!='.':
                plays[j,x]=1
            x+=1
    numWins  = np.sum(winlose, 1)
    numGames = np.sum(plays, 1)
    wp = np.divide(numWins,numGames)
    owp = []
    
    for x in range(n):
        tmp_plays = np.array(plays)
        tmp_winlose = np.array(winlose)
        tmp_plays[:,x] = 0
        tmp_winlose[:,x] = 0
        tmp_wp=np.divide(np.sum(tmp_winlose, 1),np.sum(tmp_plays, 1))
        s=0
        c=0
        for y in range(n):
            if y!=x and plays[x,y]==1:
                s+=tmp_wp[y]
                c+=1
        owp.append(s/c)

    
    oowp = []
    
    for x in range(n):
        s=0
        c=0
        for y in range(n):
            if y!=x and plays[x,y]==1:
                s+=owp[y]
                c+=1
        oowp.append(s/c)
    
    print "Case #%d:" % (i+1)
    for x in range(n):
        print 0.25 * wp[x] + 0.5 * owp[x] + 0.25 * oowp[x]
         
#    print winlose
#    print plays
#    print "wp: "
#    print wp
#    print "owp: "
#    print owp
#    print "oowp: "
#    print oowp