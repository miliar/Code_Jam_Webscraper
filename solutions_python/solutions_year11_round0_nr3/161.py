T = input()
for t in range(T):
    N = input()
    line = raw_input()
    nums = [int(i) for i in line.split()]

    if reduce(lambda x,y: x^y, nums) == 0:
        nums.sort(reverse=True)
        nums.pop()
        res = str(reduce(lambda x,y: x+y, nums))
    else:
        res = 'NO'
    
    print 'Case #%d: %s' % (t+1, res)

