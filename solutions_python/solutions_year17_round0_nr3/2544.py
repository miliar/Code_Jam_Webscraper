import sys

## Read file
cases = []
fileName = sys.argv[1]
with open(fileName) as f:
    case_number = int(f.readline())
    for i in range(0,case_number):
        this_case = f.readline().split(' ')
        int_list = [int(x) for x in this_case]
        cases.append(int_list)

## Find out max region
def maxRegion(occupy_list):
    my_list = sorted(occupy_list)
    max_region = [0,0]
    for index in range(0, len(my_list)-1):
        dist = my_list[index+1] -  my_list[index]
        if dist > (max_region[1] - max_region[0]):
            max_region[0] = my_list[index]
            max_region[1] = my_list[index+1]
    return max_region
#test = [273,14,51,3,1,9,150]
#print sorted(test)
#print maxRegion(test)

## Stall Dist
def stallDist(N,K):
    ''' Calculate stall min max decision making value'''
    # Initialize
    occupy = []
    occupy.append(-1)
    occupy.append(N)
    # Insert people
    for i in range(0, K-1):
        max_region = maxRegion(occupy)
        median = (max_region[0]+max_region[1])/2
        occupy.append(median)
    # Last Persion choice  
    last_region = maxRegion(occupy) 
    last_median = (last_region[0]+last_region[1])/2
    Rs = last_region[1] - last_median - 1
    Ls = last_median - last_region[0] -1
    value = []
    value.append( max(Ls,Rs) )
    value.append( min(Ls,Rs) )
    return value

## Show result
count = 0
for case in cases:
    count +=1
    result = stallDist(case[0], case[1])
    print 'Case #{}: {} {}'.format(count, result[0], result[1])
