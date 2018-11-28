


t = input()
i=0
while i<t:
    i+=1
    sol = ""
    n = input()
    j=0
    lns = []
    wp = []
    wwp = []
    owp = []
    plxa = []
    while j<n:
        j+=1
        plx = []
        ln = raw_input()
        lns += [ln]
        
        played = 0.0
        won = 0.0

        k = 0
        for c in ln:
            if c == '1':
                won +=1
                played+=1
                plx+=[k]
            if c == '0':
                played +=1
                plx+=[k]
            k+=1
        plxa += [plx]
        wp += [won/played]
        
    


    er = 0
    for x in plxa:
        lwp = 0.0
        for xi in x:
            played = 0.0
            won = 0.0

            k = 0
            for c in lns[xi]:
                if k!=er:
                    if c == '1':
                        won +=1
                        played+=1
                      
                    if c == '0':
                        played +=1
             
                k+=1
            lwp +=won/played
   
        if played > 0.0:
            owp += [lwp/len(x)]
        else:
            owp+=[0.0]
                
        er +=1



    oowp = []

    for x in plxa:
        lwp = 0.0
        for xi in x:
            lwp+=owp[xi]

   

        oowp += [lwp/len(x)]

                






    
##    for x in plxa:
##        sm = 0.0
##        div = 0.0
##
##
##        for xi in x:
##               
##            sm+=wp[xi]
##            
##            if lns[er][xi] == '1':
##                sm-= 1/len(x)
##            else:
##                sm+= 1/len(x)
##            div = div + 1
##
##        
##        owp+=[sm/div]
##        er+=1
##    print owp
##    oowp = []
##
##    for x in plxa:
##        sm = 0.0
##        div = len(x)
##        for xi in x:
##            sm+=owp[xi]
##        oowp+= [sm/div]
##
    sol = []
    er = 0
    for w in wp:
        sol+= [w*0.25+0.5*owp[er]+0.25*oowp[er]]
        er+=1
##    
##
##    
##        
    




    print "Case #"+str(i)+":"
    for s in sol:
        
        print s


    
    
    
