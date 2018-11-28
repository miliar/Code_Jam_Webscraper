with open('B-large.in', 'r') as fp:
    N = int(fp.readline())
    for num, line in zip(range(1, N+1), fp):
        nums = line.split(" ")
        n = nums[0]
        S = int(nums[1])
        p = int(nums[2])
        t = nums[3:]
        res = 0
        good = range(3*p-2,30+1)
        for x in map(int,t):
            if x == 0 and p != 0:
                continue
            if x in good:
                res += 1
            elif S > 0 and (int(x) in range(3*p-4, 30+1)):
                res += 1
                S -= 1 
        print 'Case #' + str(num) + ':', res
            
        
