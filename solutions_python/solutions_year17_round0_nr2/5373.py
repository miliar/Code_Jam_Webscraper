import math
x = int(input())
ans= []

for i in range(0,x):
        
        temp = input()
        temp1 = int(temp)
        
        while temp1>0:
                hello = []
                evaluate = temp1
                
                while evaluate>0:
                    hello.append(evaluate%10)
                    evaluate=evaluate//10
                hello.reverse()
                answer = all(a <= b for a,b in zip(hello, hello[1:]))
                
                if answer :
                    
                    ans.append(hello)
                    break
                
                temp1 = temp1-1
                
p = 1
for val in ans:
    output= 'Case #'+str(p)+': '+''.join(map(str,val))
    print(output)
    p=p+1
    
