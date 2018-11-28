num = raw_input()
num = int(num)
for x in range(num):
    output = "Case #"+str(x+1)+': '
    lis = raw_input().split()
    p = int(lis[0])
    s = 0
    add = 0
    for n in range(p+1):
        now = int(lis[1][n])
        if s<n:
            add += n-s
            s = n
        s+=now
    print(output + str(add))
        
        
