def gcd(a,b):
    return a if b==0 else gcd(b, a%b)
def gpf(nums={}):
    factors =[]
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            factors.append(abs(nums[i]-nums[j]))
    return factors

with open('B-small-attempt0.in') as input:
    cases = int(input.readline())
    for i in range(1,cases+1):
        case=input.readline().split(" ")
        n = int(case[0])
        events = []
        for j in range(0,n):
            events.append(int(case[j+1]))
        factors = gpf(events)
        common = factors[0]
        for j in range(1,len(factors)):
            common = gcd(common,factors[j])
        largest = max(events)
        if not (largest%common==0):
            anniversary = (int(largest/common)+1)*common
            time = anniversary - largest
        else:
            time =0
        print('Case #{}: {}'.format(i,time))
        
