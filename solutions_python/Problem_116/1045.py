
def solv(x):
    #if x!=5:
     #   return
    #print array
    
    for k in xrange(4):
        #print 'checking raws'
        val=1
        if array[k][0]!='T':
            temp=array[k][0]
        else:
            temp=array[k][1]
        if temp=='.':
            continue
        for l in xrange(4):
            if array[k][l]==temp or array[k][l]=='T':
                pass
            else:
                val=0
        if val==1 and(temp=='O'or temp=='X'):
            #print 'Case '+str(x+1)+temp+' won'
            wfile.write('Case #'+str(x+1)+': '+temp+' won\n')
            return   
    k=0
    l=0   
    for k in xrange(4):
        #print 'checking colomns'
        val=1
        if array[0][k]!='T':
            temp=array[0][k]
        else:
            temp=array[1][k]
        #print temp
        if temp=='.':
            continue
        for l in xrange(4):
            if array[l][k]==temp or array[l][k]=='T':
                pass
            else:
                val=0
        if val==1 and(temp=='O'or temp=='X'):
            #print 'Case '+str(x+1)+temp+' won'
            wfile.write('Case #'+str(x+1)+': '+temp+' won\n')
            return  
            
            
    l1=[array[0][0],array[1][1],array[2][2],array[3][3]]
   # print l1
    if l1[0]=='T':
        temp=l1[1]
    else:
        temp=l1[0]
    #print temp
    for d in l1:
        val=1
        #print d
        if d!=temp and d!='T':
            val=0
            break
    if val==1 and(temp=='O'or temp=='X'):
        #print 'Case '+str(x+1)+temp+' won'
        wfile.write('Case #'+str(x+1)+': '+temp+' won\n')
        return
      
         
    l2=[array[0][3],array[1][2],array[2][1],array[3][0]]
    #print l2
       
    if l2[0]=='T':
        temp=l2[1]
    else:
        temp=l2[0]
    #print temp
    for d in l2:
        val=1
        if d!=temp and d!='T':
            val=0
            break
    if val==1 and(temp=='O'or temp=='X'):
        #print 'Case '+str(x+1)+'#'+temp+' won'
        wfile.write('Case #'+str(x+1)+': '+temp+' won\n')
        return
           
    k=0
    l=0
    for k in xrange(4):
        
        for l in xrange(4):
            if array[k][l]=='.':
                #print 'not complete'
                wfile.write('Case #'+str(x+1)+': Game has not completed\n')
                return
                
    #print 'draw'
    wfile.write('Case #'+str(x+1)+': Draw\n')
    
        
        
    


file=open('A-small-attempt0.in','r')
wfile=open('output11','w')
number_of_cases= int(file.readline())
counter=0;

for x in xrange(number_of_cases):
    #print x
    raws=4
    colomns=4
    array=[[0 for i in range(4)] for j in range(4)] 

    for i in xrange(raws):
        temp_l=list(file.readline())
        #print len(temp_l)       
        if len(temp_l)==5:
            #if len(temp_l)==1:
             #   print 'length is fucking 1'
            for j in xrange(colomns):                
                array[i][j]=temp_l[j]
        print array[i]
    list(file.readline())
    solv(x)
    #break
    
