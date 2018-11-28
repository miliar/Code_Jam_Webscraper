import sys, math

def gcd_list(nums):
    return reduce(lambda x, y: gcd(x,y), nums, nums[0])

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a%b)
    return a

if __name__ == '__main__':
    input = open(sys.argv[1], 'r')
    output = open(sys.argv[2],'w')
    
    T = int(input.readline())
    for t in range(1,T+1):
        nums = map(int, input.readline().split())
        diffs = map(lambda x, y: abs(x-y), nums[1:-1], nums[2:])
        print diffs
        denominator = gcd_list(diffs)
        print denominator
        
        result = math.ceil(1.*nums[1]/denominator)*denominator - nums[1]
        
        output.write("Case #%d: %d \n"%(t,result))