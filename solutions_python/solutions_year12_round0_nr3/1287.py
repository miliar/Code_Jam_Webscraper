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
    
    A = int(para[0])
    B = int(para[1])
    #p = para[2]            
    y = set([])
    
    #print A,B
    for i in range(A,B-1):
        k = str(i)
        #print len(k)
        for j in range(1,len(k)):
            
            z = k[-j:]+k[:-j]
            #print k, z ,j
            if int(z) <= B and int(z) >= A and z != k and len(str(int(z)))==len(k):
                y.add((min(int(z),i),max(i,int(z))))
                #y.add((z,k))
                #print "z",z
    
    #print "res:",y/2+y%2,y 
    #print y
    return len(y)
    #return str(y/2+y%2)
#print translate("10 40")
get_problems()   

