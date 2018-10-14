t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    num = 0
    n = str(input())
    
    if (len(n)==1):
        num = n
    else:
        n2 = int(n)
        
        for k in range(n2,9,-1):
            n = str(k)
            x = 0
            for j in range(len(n)):
                y = int(n[j])
                if(y>=x):
                    x=y
                    if(j==(len(n)-1)):
                        num = (int(n))
                        break
                else:
                    break

            if (num==int(n)):
                break
            else:
                continue

    print("Case #{}: {} ".format(i,num))
 
