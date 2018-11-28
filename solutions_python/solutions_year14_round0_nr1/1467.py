with open("A-small-attempt1.in", "r") as f:
    num_case = int(f.readline())
    #lst.append(f.readline().split())
  
    for n in range(1, num_case + 1):
        row = int(f.readline())
        
        #print(row-1)           
        for i in range(0, row-1):
            f.readline()
        lst = (f.readline().split())
        for i in range(0, 4-row):
            f.readline()

        row = int(f.readline())  
        #print("row ",row) 
       
        for i in range(0, row-1):
            f.readline()
        slst = (f.readline().split())

       # for i in range(0,4):
       #     print(slst[i])
            
        for i in range(0, 4-row):
            f.readline()
        
        cnt = 0
        idx = -1;
        for i in lst:
            for j in slst:
                if(i == j):
                    cnt = cnt+1
                    idx = i
                    #print ("j " , i)

        if(cnt == 1):
            print("Case #{0}: {1}".format(n, idx))
        elif(cnt >= 2):
            print("Case #{0}: Bad magician!".format(n))
        elif(cnt==0):
            print("Case #{0}: Volunteer cheated!".format(n))

        
    
