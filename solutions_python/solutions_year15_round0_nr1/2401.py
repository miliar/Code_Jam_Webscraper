def process(case, nums):
    p = 0;
    required = 0;
    for i in range(len(nums)):
        if p >= i:
            p += nums[i]
        else:
            required += i - p
            p = i + nums[i]
    print "Case #%d: %d" %(case, required)

with open('qa.large', 'r') as f:
    num = int(f.readline().strip())
    for i in range(num):
        chunks = f.readline().strip().split()
        nums = [int(x) for x in chunks[1]]
        process(i + 1, nums)
        
