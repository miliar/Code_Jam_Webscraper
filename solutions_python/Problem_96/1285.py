def get_problems():
    f = file("A-small-attempt0.in")
    f2 = open("A-small-attempt0.out", 'w')
    numCases = f.readline()
    for i in xrange(1, int(numCases)+1):
        line = f.readline()
        output = translate(line)
        stra = "Case #%d: %s\n" % (i, output)        
        f2.write(stra)
    f2.close()
        
        
def translate(line): 
    i = 0
    para = []
    while True:
        t= line.find(" ",i) 
        if t != -1:
            para.append(int(line[i:t]))
            i =t+1
        else:
            para.append(int(line[i:]))
            break
    
    N = para[0]
    S = para[1]
    p = para[2]            
    y = 0
    for score in para[3:]:
        k = score/3
        r = score % 3
        #print "score:",score,k,r
        if k >= p or (k + min(r,1)) >= p:
            y+=1
        #    print "norm"
        elif k+r >= p and S:
            y+=1
            S-=1
        #    print "sup1"
        elif k+1 >= p and k >0 and S:
            y+=1
            S-=1
        #    print "sup2"
        #print "nextscore"  
    #print "nextline" 
    return str(y)
        
get_problems()   

