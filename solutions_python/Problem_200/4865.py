n=int(input())
nos=[]
for i in range(n):
    nos.append(int(input()) )

def areSorted(n):
    next_digit = n%10
    n = n/10
    while (n):
        digit = (int(n%10))
        if (digit > next_digit):
            return False
        next_digit = digit
        n = n/10
    
    return True

k=1
for i in nos:
    for j in range(i,-1,-1):
        if(areSorted(j)):
            print("Case #{}: ".format(k),j)
            k+=1
            break


    
    
