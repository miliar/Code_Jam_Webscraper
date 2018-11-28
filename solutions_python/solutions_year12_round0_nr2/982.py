def dancing(value,n_surp,limit):
    division=value/3
    reminder=value%3
    if division==0 and reminder==0 and division<limit:
        return False,n_surp
    if reminder==0:
        if division>=limit:
            #print "1. ",value,division,n_surp
            return True,n_surp
        elif n_surp>0 and division+1>=limit:
            #print "2. ",value,division+1,n_surp-1
            return True,n_surp-1
    elif reminder==1:
        if division+1>=limit:
            #print "3. ",value,division+1,n_surp            
            return True,n_surp
        #elif n_surp>0 and division>0 and division+2>=limit:
        #    print "4. ",value,division+2,n_surp-1            
        #    return True,n_surp-1
    elif reminder==2:
        if division+1>=limit:
            #print "3. ",value,division+1,n_surp            
            return True,n_surp
        elif n_surp>0 and division+2>=limit:
            #print "4. ",value,division+2,n_surp-1            
            return True,n_surp-1    
    return False,n_surp

f = open('B-large.in','r')
#f = open('B-large.in','r')
arr= f.readlines()
f.close()

f=open('B.out','w')
for case in range(1,int(arr[0])+1):
#for case in range(59,60):
    countlarge=0
    
    line=arr[case].split()
    n_case=int(line[0])
    n_surprising=int(line[1])
    limit_value=int(line[2])

    for i in range(3,3+n_case):
        boole,n_surprising=dancing(int(line[i]),n_surprising,limit_value)
        if boole:
            countlarge=countlarge+1
    #print "Case #"+str(case)+": "+str(countlarge)
    f.write("Case #"+str(case)+": "+str(countlarge)+"\n")

f.close()  
