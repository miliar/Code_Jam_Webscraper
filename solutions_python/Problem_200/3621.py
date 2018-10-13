n=input()

for i in range(n):
    
    
    num=input()
    num=str(num)
    while(num>=0):
        arr=[]
        
        if (len(num)==1):
            print("Case #"+str(i+1)+": "+num)
            break
        for j in range(len(num)):
            arr.append(int(num[j]))

        if sorted(arr)==arr:
            print("Case #"+str(i+1)+": "+num)
            break
        
        num=str(int(num)-1)
    
            
