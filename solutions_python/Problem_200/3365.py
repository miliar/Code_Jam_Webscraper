T=input()
N=1
while T > 0:
    num = map(int, list(raw_input().strip("\r\n")))
    def nine(i):
        global num
        for i in range(i, len(num)):
            num[i] = 9
    def minus(i):
        global num
        if num[i] == 0:
            num[i] = 10
            minus(i-1)
        num[i] -= 1
    while True:
        for i in range(len(num) - 1):
            if num[i] > num[i+1]:
                minus(i)
                nine(i+1)
                break
        else:
            break
                
    print "Case #{}: {}".format(N, int("".join(map(str, num))))
    N += 1
    T -= 1
