import math
import fractions
file1=open('input.txt')
file2=open('output.txt','w')
T=int(file1.readline())
for ind in range(1,T+1):
    x=file1.readline()
    two=0
    num1=0
    num2=0
    count=1
    for i in range(0,len(x)):
        if two==0 and x[i]!='/':
            num1=(num1*10)+int(x[i])
        elif two==1 and str.isdigit(x[i]):
            num2=(num2*10)+int(x[i])
        elif two==0:
            two=1
        else:
            break
    x=fractions.gcd(num1,num2)
    num2=num2/x
    num1=num1/x
    if math.log(num2,2)!=int(math.log(num2,2)):
        file2.write('Case #' + `ind` + ': impossible\n')
    else:
        while num2>2*num1:
            count+=1
            num2/=2
        file2.write('Case #' + `ind` + ': ' + `count` + '\n')
            
        
