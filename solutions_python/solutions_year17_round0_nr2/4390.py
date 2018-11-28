def istidy(number):
    number=str(number)
    qwe=list(number)
    for k in range(0,len(qwe)-1):
        if int(qwe[k])>int(qwe[k+1]):
            return False
    return True


cnt=1

num=int(input())
for i in range(1, num+1):
    ip=int(input())
    for i in range(ip, 0, -1):
        res = istidy(i)
        if res == True:
            print("Case #{}: {}".format(cnt,i))
            cnt += 1
            break
