fin = open('A-large.in','r')
fout = open('A-large.out','w')

ls = [e.strip() for e in fin.readlines()]
n= int(ls[0])

count = 1
for ca in xrange(n):
    ## each search
    
    s = int(ls[count])
    count+=1
    engines = ls[count:count+s]
    count+=s
    #print s,engines   
    q = int(ls[count])
    count+=1       
    quer = ls[count:count+q]
    if quer:
        quer.append(quer[-1])
    else:
        quer = engines[0]
    count+=q

    uni = {}
    for e in engines:
        uni[e]=1
    cur = uni.copy()
    change= 0
    
    for x in xrange(len(quer)-1):   
        if quer[x] in cur:
            del cur[quer[x]]
        if (len(cur)==1 and (quer[x+1] in cur)):
            print "on "+str(quer[x+1])
            cur = uni.copy()
            change+=1
            
            

        
    fout.write("Case #"+str(ca+1)+": "+str(change)+"\n")


fout.close()
fin.close()
