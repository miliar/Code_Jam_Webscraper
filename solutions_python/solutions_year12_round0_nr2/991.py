f1=open("in")
f2=open('out','w')

loop=int(f1.readline())

for ii in range(1,loop+1):
    line=f1.readline().split()
    print line
    no_of_goo=int(line[0])
    no_of_sup=int(line[1])
    avg=int(line[2])
    count=0
    
    
    for i in range(3,3+no_of_goo):
        no=int(line[i])
        if no != 0:
            div3 = no/3
            if div3 >= 1:
                print div3,no
                if(no%3==0 and div3 >= avg):
                    print '1'
                    count=count+1
                elif(no%3==0 and div3+1 >= avg and no_of_sup > 0):
                    print '2'
                    count=count+1
                    no_of_sup=no_of_sup-1
                if(no%3==2 and div3 >= avg):
                    print '3'
                    count=count+1
                elif(no%3==2 and div3+1 >= avg):
                    print '4'
                    count=count+1
                elif(no%3==2 and div3+2 >= avg and no_of_sup > 0):
                    print '5'
                    count=count+1
                    no_of_sup=no_of_sup-1
                if(no%3==1 and div3 >= avg):
                    print '6'
                    count=count+1
                elif(no%3==1 and div3+1 >= avg):
                    print '7'
                    count=count+1
            elif div3 < 1:
                if(no==1 and no>=avg):
                    count=count+1
                if(no==2 and no >= avg and no_of_sup > 0):
                    print '3'
                    no_of_sup=no_of_sup-1
                    count=count+1
        elif no==0 and avg==0:
            count=count+1 
                    
    print '\n\n',count
    print no_of_sup
    toprint = "Case #"+str(ii)+': '+str(count)+'\n'
    f2.write(toprint)
        
        
        
        
            
         