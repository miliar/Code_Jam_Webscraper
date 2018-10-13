n=input()
for i in range(n):
    arr,k=raw_input().split()
    arr=list(arr)
    k=int(k)
    
    
    
    count=0
    for j in range(len(arr)-k+1):
        if arr[j]=='+':
            continue
        else:
            
            for m in range(j,j+k):
                
                if arr[m]=='+':
                    arr[m]='-'
                else:
                    arr[m]='+'

            count=count+1
            


    else:
        
        if '-' in arr:
            print "Case #"+str(i+1)+": IMPOSSIBLE"

        else:
            print "Case #"+str(i+1)+": "+str(count)

            


    
        
