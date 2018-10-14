def check(num):
    return sorted(num)==num

T=int(input())
case=1
while case<=T:
    num=input()
    num=list(num)
    while not check(num):
        le=len(num)
        for i in range(le-1,0,-1):
            if num[i]<num[i-1]:
                num[i-1]=str(int(num[i-1])-1)
                num=num[:i]+['9']*(le-i)
    num=int(''.join(x for x in num))
    print("Case #{0}: {1}".format(case,num))
    case+=1
