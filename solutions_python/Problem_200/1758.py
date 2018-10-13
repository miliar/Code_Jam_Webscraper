# @Author: Tushar Jain <tshrjn>
# @Date:   2017-04-09T03:02:21+05:30
# @Filename: tidy.py
# @Last modified by:   tshrjn
# @Last modified time: 2017-04-09T03:55:56+05:30

def checktidy(n):
    prev = 0
    for current in str(n):
        # print(current)
        if int(current) < prev:
            return False
        prev = int(current)
    return True

def tidyhelper(n):
    prev = 0
    n = str(n)
    for idx, current in enumerate(n):
        # print (int(current) < prev:
        if int(current) < prev:
            # print(idx)
            n = n[:idx-1] + str(int(prev) - 1) + ''.join([str(9)]*(len(n) - idx))
            # print(n)
            break
        prev = int(current)
    return n

def tidyup(n):
    flag = True
    while flag:
        n = tidyhelper(n)
        # print(n, checktidy(n))
        if checktidy(n):
            # print("flag off")
            flag = False
    return n

t = int(input())
for i in range(t):
    n = int(input())
    ans = tidyup(n)
    print("Case #{}: {}".format(i+1 , int(ans)))
