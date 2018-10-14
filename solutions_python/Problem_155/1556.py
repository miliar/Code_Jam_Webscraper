for x in range(int(input())):
    n, l = input().split()
    n = int(n)
    l = [int(z) for z in l]
    count = l[0]
    extra = 0
    for i in range(n + 1):
        if (i != 0):
            val = l[i]
            if (val == 0):
                continue
            elif (i <= count):
                count += val
            else:
                extra += i - count
                count += i - count + val
    print ("Case #%d: %d" %(x + 1, extra))
    




