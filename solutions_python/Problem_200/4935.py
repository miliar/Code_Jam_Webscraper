def tidy_num(last):
    if last in range(1,10):
        return last
    else:
        for yum in reversed(range(1,last + 1)):
            num = yum
            while(num != 0):
                rem1 = num % 10
                num = num // 10
                rem2 = num % 10
                if rem1 < rem2:
                    break
            else:
                return yum
                break


t = int(input())
for i in range(1, t + 1 ):
    n = int(input())
    print("Case #{}: {}".format(i, tidy_num(n)))
