cases=[]
vals=[]
addition=[]
testcase=int(input(""))

for i in range(0,int(testcase)):
    cases=input("").split(" ")
    #print(cases)
    vals=list(cases[0])
    times=int(cases[1])
    #print(vals)
    for j in range(0,len(vals)):
        if vals[j] is "+":
            vals[j]=1
        else:
            vals[j]=0
    for j in range(0,len(vals)):
        if vals[j] is 1:
            flag=1
        else:
            flag=0
            break
    if flag is 1:
        print ("Case #"+str(i+1)+": 0")
    else:
        y=len(vals)
        count=0
        for j in range(0,y):
            #print(vals)
            if (j+times)<=y:
                if vals[j] is 0:
                    count=count+1
                    for l in range(0,times):
                        if vals[l+j] is 0:
                            vals[l+j]=1
                        else:
                            vals[l+j]=0
        for j in range(0,len(vals)):
            if vals[j] is 1:
                flag=1
            else:
                flag=0
                break
        if flag is 1:
            print ("Case #"+str(i+1)+": "+str(count))
        else:
            print ("Case #"+str(i+1)+": IMPOSSIBLE")
            
            
        
        
            
