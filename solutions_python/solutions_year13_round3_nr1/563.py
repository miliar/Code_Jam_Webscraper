file=open('in','r')
wfile=open('output01','w')
number_of_cases= int(file.readline())

for i in xrange(number_of_cases):
    fulline=file.readline().split()
    fulstr1=fulline[0]
    n=int(fulline[1])
    
    nvaleu=0
    
#    print fulstr1
    for j in xrange(len(fulstr1)):
            substr=fulstr1[j:]
#            print substr
            count=0
            if(len(substr)>=n):
                for k in substr:
    #                print k
                    
                    if(k!='a' and k!='e' and k!='i' and k!='o' and k!='u'):
                        count+=1
                    else:
                        count=0
                    if (count>=n):
        #                print substr
        #                print count
                        nvaleu+=1
                        break


    for l in xrange(len(fulstr1)):
        fulstr=fulstr1[0:-l]
#        print fulstr
        for j in xrange(len(fulstr)):
            substr=fulstr[j:]
#            print substr
            count=0
            if(len(substr)>=n):
                for k in substr:
    #                print k
                    if(k!='a' and k!='e' and k!='i' and k!='o' and k!='u'):
                        count+=1
                    else:
                        count=0
                    if (count>=n):
        #                print substr
        #                print count
                        nvaleu+=1
                        break
                
    wfile.write('Case #'+str(i+1)+':'+str(nvaleu)+'\n')
            
        
        
        
