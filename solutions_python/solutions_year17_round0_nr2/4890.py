t = int(input())
filewrite = open("output1.txt", "w")
for z in range(t):
    y = int(input())
    n = [int(temp) for temp in str(y)]
    
    if(len(n)==1):
        filewrite.write("Case #"+str(z+1)+": "+str(y)+"\n")
        print("Case #"+str(z+1)+": "+str(y))
    else:
        while(y>=0):
            flag=0
            for i in range(0,len(n)-1):
                if(n[i]>n[i+1]):
                    flag=1
                    break
            if(flag==0):
                filewrite.write("Case #"+str(z+1)+": "+str(y)+"\n")
                print("Case #"+str(z+1)+": "+str(y))
                break
            else:
                y=y-1
                n=[int(temp) for temp in str(y)]
    
filewrite.close()
