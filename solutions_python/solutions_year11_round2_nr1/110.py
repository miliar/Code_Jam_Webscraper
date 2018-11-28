incoming=open('A-large.in')
output=open('A-largeoutput0.txt','w')
T=int(incoming.readline())
for i in range(1,T+1):
    teams = int(incoming.readline())
    A={}
    wp={}
    owp={}
    oowp={}
    rpi=[]
    for k in range(teams): # particular team
        A[k]=incoming.readline().rstrip()
        totalplay = 0
        totalwin = 0
        for t in range(teams): #team's games?
            if A[k][t] == '.':
                pass
            else:
                s=int(A[k][t])
                totalplay+=1
                totalwin+=s
        wp[k]=totalwin/totalplay
    for k in range(teams): # my team
        counts=0
        summing = 0
        for t in range(teams): # calculate team t
            if A[k][t] != '.':
                counts+=1
                hiswin = 0
                hisplay = 0
                for j in range(teams):
                    if A[t][j] == '.' or j == k:
                        continue
                    elif A[t][j]=='1':
                        hiswin+=1
                    hisplay+=1
                hisowp = hiswin/hisplay
                summing +=hisowp
        owp[k]=summing/counts

    for k in range(teams):
        counts=0
        summing = 0
        for t in range(teams):
            if A[k][t] != '.':
               counts+=1
               summing += owp[t]
        oowp[k]=summing/counts
    for k in range(teams):
        rpi.append(0.25*wp[k]+0.5*owp[k]+0.25*oowp[k])
            

    output.write("Case #%d:\n"%i)
    for k in range(teams):
        output.write("%.12f\n"%rpi[k])
    
incoming.close()
output.close()
