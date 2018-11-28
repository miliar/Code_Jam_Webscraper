n = int(raw_input(''))

for p in range(n):
    nums = raw_input('').split()
    n = int(nums[0])
    l = int(nums[1])
    h = int(nums[2])

    
    others = raw_input('').split()


    flag = 0
    for i in range(l,h+1):
        #print i
        for j in range(n):
            if i % int(others[j]) != 0 and int(others[j]) % i != 0:
                flag = 1
                break
        if not flag:
            print '''Case #%d: %d''' % (p+1,i)
            flag = 2
            break
        flag = 0
    if flag != 2:
        print '''Case #%d: NO''' % (p+1)
    
