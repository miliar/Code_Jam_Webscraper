fp = open("A-small-attempt4.in")
fx = open("out.txt",'w+')
t = int(fp.readline())
for case in range(t):
    line1=fp.readline().strip()
    
    L1 = []
    for ch in line1:
        L1.append(ch)
        
 
    line2=fp.readline().strip()
    L2 = []
    for ch in line2:
        L2.append(ch)

 

    line3=fp.readline().strip()
    L3 = []
    for ch in line3:
        L3.append(ch)

        
    line4=fp.readline().strip()
    L4 = []
    for ch in line4:
        L4.append(ch)

   
    """ prev="7"
    cnt=0
    l="2"
    for i in L:
        cnt=0
        for mov in i:
            if prev==mov and prev!=".":
                cnt+=1
                l=prev
            prev=mov
    print(cnt)"""
    
    L=[L1,L2,L3,L4]
    #print(L)
    
    prev="7"
    cnt=0
    l="2"
    for i in L:
        cnt=0
        prev="7"
        for mov in i:
            if (prev==mov and prev!=".") or mov=="T":
                cnt+=1
            if cnt==3:
                l=prev
            elif prev!=mov:
                cnt=0
            prev=mov
           
            
    if l=="2":
        L1=[]
        L2=[]
        L3=[]
        L4=[]
        for i in range(4):
            L1.append(L[i][0])
        for i in range(4):
            L2.append(L[i][1])
        for i in range(4):
            L3.append(L[i][2])
        for i in range(4):
            L4.append(L[i][3])
        K=[L1,L2,L3,L4]
       # print(K)
            
        prev="7"
        cnt=0
        l="2"
        
        for i in K:
          cnt=0
          prev="7"
          for mov in i:
            if (prev==mov and prev!=".") or mov=="T":
                cnt+=1
            if cnt==3:
                l=prev
            elif prev!=mov:
                cnt=0
            prev=mov

    if l=="2":
        prev="7"
        cnt=0
        l="2"
        for i in range(4):
            if (prev==L[i][i] and prev!=".") or L[i][i]=="T": 
                cnt+=1
            if cnt==3 or (cnt==2 and L[0][0]=="T"):
                l=prev
            elif prev!=L[i][i] and L[i][i]!="T" :
                cnt=0
                prev=L[i][i]
           
    if l=="2":
        prev="7"
        cnt=0
        l="2"
        n=3
        for i in range(4):
  
            if (prev==L[i][n] and prev!=".") or L[i][n]=="T":
                cnt+=1      
            if cnt==3 or (cnt==2 and L[0][3]=="T"):
                l=prev
            elif prev!=L[i][n] and L[i][n]!="T":
                cnt=0
                prev=L[i][n]
           
            n-=1
        
        
    if l!="2":
        print("Case #"+str(case+1)+": "+l+" won",file=fx)


        
    else:
        flag=0
        for i in L1:
            if i==".":
                flag=1
        for i in L2:
            if i==".":
                flag=1
        for i in L3:
            if i==".":
                flag=1
        for i in L4:
            if i==".":
                flag=1
        if flag:
            print("Case #"+str(case+1)+": "+"Game has not completed",file=fx)
                
        else:
            print("Case #"+str(case+1)+": "+"Draw",file=fx)
       

            
        """if (len(set(L1))) == 4: 
             print("Case #"+str(case+1)+": "+"Draw",file=fx)
        elif (len(set(L2))) == 4: 
             print("Case #"+str(case+1)+": "+"Game has not completed",file=fx)
        elif (len(set(L3))) == 4: 
             print("Case #"+str(case+1)+": "+"Game has not completed",file=fx)
        elif (len(set(L4))) == 4: 
             print("Case #"+str(case+1)+": "+"Game has not completed",file=fx)"""
        

    x=fp.readline()
        
    #print("Case #"+str(case+1)+": ",file=fx)    
fp.close()
fx.close()
