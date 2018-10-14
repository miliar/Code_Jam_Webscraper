tc  = int(input())
for i in range(1,tc+1):
    stall,user = input().split(' ')
    stall = int(stall)
    user= int(user)
    lst= []
    while True :
        if user != 1:
            res = stall // 2
            larg = stall - res
            small = stall - larg
            lst.append(larg - 1)
            lst.append(small)
            stall = max(lst)
            lst.remove(max(lst))
        else:
            res = stall // 2
            larg = stall - res
            small = stall - larg
            print("Case #%d: "%i+str(small)+" "+str(larg-1))
            break
        user  = user -1
