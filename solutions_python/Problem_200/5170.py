def tidy_check(num):
    if num%10 != 0:
        temp = 9
        while(num>0):
            dig = num%10
            if dig<=temp:
                num = num//10
                temp = dig
            else:
                return -1
        return 1
    else:
        return -1

t = int(input())
for a0 in range(t):
    n = int(input())
    if n<10:
        print('Case #'+str(a0+1)+': '+str(n))
    else:
        while(1):
            ans = tidy_check(n)
            if ans==-1:
                n -= 1
            else:
                print('Case #'+str(a0+1)+': '+str(n))
                break