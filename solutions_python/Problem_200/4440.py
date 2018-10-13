import math

testcases=int(input(""))


for i in range(0,testcases):
    maxn=0
    num=[]
    n=input("")
    an=int(n)
    num=list(n)
    #print(num)
    flag=0
    num=list(map(int,num))
    for j in range(0,len(num)):
        if num[j] >= maxn:
            maxn=num[j]
        else:
            flag=1
            break
    #print(maxn)
    if flag is 1:            
        for j in range(0,len(num)):
            if num[j] is maxn:
                #print(j)
                cal=[]
                for l in range(j+1,len(num)):
                    cal=cal+[num[l]]
                break
        #print(cal)
        mul=0
        for j in range(0,len(cal)):
            #print(mul)
            mul=mul+(cal[len(cal)-j-1]*math.pow(10,j))
        val=len(num)-len(cal)
        #print(val)
        #print(num[val])
        mul=int(mul)
        an=an-mul-1
        num=list(map(int,list(str(an))))
        #print(num[val-1])
        if (num[val-1]) is 0:
            mul=-1
            for j in range(0,val):
                mul=mul+(1*math.pow(10,j))
            an=an-int(mul)
        #print(mul)
        #print(an)
        
    print ("Case #"+str(i+1)+": "+str(an))
        
            
                
    
    
