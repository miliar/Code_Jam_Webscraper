
fname="B-large.in"

inputF=open(fname,'r+')
outF=open('outputblarg','w+')

T=int(inputF.readline())
for i in xrange(T):
    x=str(i+1)
    linei=inputF.readline().split()
    #~ print linei
    C,F,X=float(linei[0]),float(linei[1]),float(linei[2])
    
    t=0
    i=0
    tPrev= float("inf")
    
    while 1:
        tTotal=X/(2+(i*F))+t
        #~ print tTotal
        if tPrev<tTotal:
            outF.write('Case #'+str(x)+': '+str(tPrev)+'\n')
            #~ print 'Case #'+str(x)+': '+str(tPrev)
            break
        else:
            tPrev=tTotal
            t+=C/(2+(i*F))
        i+=1
    
    #~ print C,F,X
    
        #~ outF.write('Case #'+x+': Bad magician!\n')
    #~ print A,B

inputF.close()
outF.close()
