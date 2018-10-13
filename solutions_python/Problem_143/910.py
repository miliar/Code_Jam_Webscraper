file=open("magic.txt","r")
test = int(file.readline().strip())
c=1
count=0
while test!=0:
    count=0
    nums=[]
    nums=file.readline().strip().split()
    A=int(nums[0])
    B=int(nums[1])
    K=int(nums[2])

    for i in range(0,A):
        for j in range(0,B):
            
            ans=i&j
            if ans<K:
                count=count+1
  
           
                
    print("Case #",end='')
    print(c,end='')
    print(": ",end='')
    print(count)

    test=test-1
    c=c+1
