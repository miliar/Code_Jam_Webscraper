case = int(input())
for test in range(1,case+1):
    num = int(input())
    flag = False
    while flag == False:
        strnum = str(num)
        n = len(strnum)
        c = 1
        flag = True
        for i in range(n-1):
            if strnum[n-i-2] > strnum[n-i-1]:
                flag = False
                num -= c * (int(strnum[n-i-1]) + 1)
                num -= num % c
                num += c - 1
                break
            c *= 10
    print("Case #{}: {}".format(test, num))
