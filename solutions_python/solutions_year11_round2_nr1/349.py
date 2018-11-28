'''
Created on 2011/5/22

@author: ckchen
'''


filename = "../A-large.in"
file=open(filename)

taskN = int(file.readline())

for k in range(1,taskN+1):
    team = int(file.readline())
    map = {}
    for i  in range(0,team):
        map[i]={}
        str = file.readline()
        #print str
        for j in range(0,team):
            map[i][j]=str[j]
     
#    for i  in range(0,team):
#        for j in range(0,team):
#            print map[i][j],
#        print ""
            
    wp = {}
    tolL = {}
    winL = {}
    for i in range(0,team):
        win = 0
        tol = 0
        for j in range(0,team):
            if map[i][j]=='1':
                win+=1
                tol+=1
            elif map[i][j]=='0':
                tol+=1
        tolL[i]=tol
        winL[i]=win
        wp[i]=win/float(tol)
#    print "wp"    
#    for i in range(0,team):
#        print wp[i]    
        
    owp = {}    
    for i in range(0,team):
        total_wp = 0.0
        tol=0
        for j in range(0,team):
            if map[i][j]=='1' :
               total_wp+= (winL[j])/float(tolL[j]-1)
               tol+=1 
            elif map[i][j]=='0' :
               total_wp+= (winL[j]-1)/float(tolL[j]-1)
               tol+=1 
        owp[i]=total_wp/float(tol)     
    
    oowp={}    
    for i in range(0,team):
        total_owp = 0.0
        tol=0
        for j in range(0,team):
            if not map[i][j]=='.':
               total_owp+=owp[j]
               tol+=1
        oowp[i]= total_owp/tol
#    print "owp"
#    for i in range(0,team):
#        print owp[i]   
    
    print "Case #%d:"%k    
    for i in range(0,team):
        RPI = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]
        print  RPI   
                
        
           
    