from itertools import combinations
used_bits = 20

def pat_sum(a,b):
    mask = 1
    sum = 0
    for i in range(0,used_bits):
        sum += ((a & mask) ^ (b & mask))
        mask <<= 1
    return sum

file_name = 'C-small-attempt1'
file = open(file_name + '.in', 'r')
out_file = open(file_name + '.out', 'w')

lines = [l.strip() for l in file]
num_cases = int(lines.pop(0))


for case_num in range(1, num_cases + 1):
    count = int(lines.pop(0))
    candies = [int(c) for c in lines.pop(0).split(' ')]
    
    keeper = None
    
    for size in range(1, count/2 + 1):
        for comb in combinations(range(0,count), size):
            stackA = [x for idx, x in enumerate(candies) if idx in comb]
            stackB = [x for idx, x in enumerate(candies) if idx not in comb]
            
            if reduce(pat_sum, stackA) == reduce(pat_sum, stackB):
                add = lambda x,y : x + y
                biggest = max(reduce(add, stackA), reduce(add,stackB))
                if keeper:
                    keeper = max(keeper, biggest)
                else:
                    keeper = biggest
    
    result = keeper or "NO"
    print case_num
    out_file.write("Case #%s: %s\n" % (case_num, result))
