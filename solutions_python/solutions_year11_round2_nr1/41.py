from fractions import Fraction

fin = open ('c:/users/hai/my projects/google code jam/2011/1B/A/A-large.in')
fout = open ('c:/users/hai/my projects/google code jam/2011/1B/A/A-large.out','w')

T = int(fin.readline())

for testcase in range(1,T+1):
    N = int(fin.readline())
    l = []
    for i in range(N):
        l.append(fin.readline())

    losses = [x.count('0') for x in l]
    wins = [x.count('1') for x in l]
    played = [losses[i] + wins[i] for i in range(N)]
    
    WP = [None]*N
    for i in range(N):
        WP[i] = Fraction (wins[i], played[i])

    OWP = []
    for j in range(N):
        tmp = 0
        c=0
        for i in range(N):
            if l[i][j] != '.':
                c+=1
                if l[i][j] == '1':
                    tmp += Fraction(wins[i]-1, played[i]-1)
                else:
                    tmp += Fraction(wins[i], played[i]-1)
        #print ('*********', tmp, c)
        OWP.append(tmp/c)

    OOWP = []
    for j in range(N):
        tmp = 0
        c = 0
        for i in range(N):
            if l[i][j] != '.':
                c += 1
                tmp += OWP[i]
        #print ('########', tmp, c)
        OOWP.append(tmp/c)

    #print ('WP : ', WP)
    #print ('OWP : ', OWP)
    #print ('OOWP : ', OOWP)
    fout.write('Case #' + str(testcase) +':\n')
    for i in range(N):
        RPI = WP[i]/4 + OWP[i]/2 + OOWP[i]/4
        #print (RPI)
        fout.write (str(float(RPI))+'\n')
    

fin.close()
fout.close()
