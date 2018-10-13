import sys
order='1023456789abcdefghijklmnopqrstuvwxyz'
sys.stdin = open('i.in')
output = open('o.txt', mode='w')
n=int(input())
for i in range(n):
    num=input()
    old=''
    new=''
    j=0
    for d in num:
        if(d not in old):
            old+=d
            new+=order[j]
            j+=1
    if(j==1):
        j=2
    num=num.translate(''.maketrans(old,new))
    print('Case #{0}: {1}'.format(i+1,int(num,j)),file=output)

        
        
    
