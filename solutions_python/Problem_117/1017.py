#print "hello world"

def solv():
    boo=1
    for i in xrange(raws):
        #temp=array[i][0]
        #boo=1
        #d_v=array[i][0]
        for j in xrange(colomns):
            d_v=array[i][j]
            for s in xrange(colomns):
                if d_v<array[i][s]:
                    for t in xrange(raws):
                        if d_v<array[t][j]:
                            boo=0
                
                
         
    if boo==1:
        wfile.write(yes)
    else:
        wfile.write(no)
        
        
        
    


file=open('B-large.in','r')
wfile=open('output1','w')
number_of_cases= int(file.readline())
#print file.readline()
#print file.readline()
#print number_of_cases
counter=0;


for x in xrange(number_of_cases):
    #boo=1;
    yes='Case #'+str(x+1)+': YES\n'
    no='Case #'+str(x+1)+': NO\n'
    second_line=str(file.readline())
    se_list=second_line.split()
    #print second_line
    #print second_line
    
    
    if len(se_list)<2:
        colomns=0
    else:
        colomns=int(se_list[1])
    raws=int(se_list[0])
    
    #if (colomns<2 or raws <2):
      
    #print "col"+str(colomns)
    #print 'raw'+str(raws)
    
    #continue

    

    array=[[0 for i in range(colomns)] for j in range(raws)]
    #print array

    for i in xrange(raws):
        temp_l=file.readline().split()
        for j in xrange(colomns):
            array[i][j]=int(temp_l[j])
    solv()   
    
