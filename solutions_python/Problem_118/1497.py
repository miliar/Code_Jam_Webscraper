def palin(num2):
    if(len(num2)>2 and num2[-2]=='.' and num2[-1]=='0' ):
        num2=num2[:-2]
    l1=len(num2)
    l2=l1/2
    for i in range(l2):
        if num2[i]!=num2[l1-i-1]:
            return False
    return True
    
f=open("C-small-attempt0.in","r")
f2=open("ans.out","w")
x=int(f.readline())
for a in range(x):
    temp=f.readline().split()
    num1=int(temp[0])
    num2=int(temp[1])
    count=0
    for i in range(num1,num2+1):
        sqrt=str(i**0.5)
        if((sqrt[-2]=='.' and sqrt[-1]=='0' )or( '.' not in sqrt)):
            if palin(sqrt)==True:
                if palin(str(i))==True:
                    count+=1
    t=a+1
    f2.write("Case #%d: %d\n"%(t,count))
f.close()
f2.close()
        