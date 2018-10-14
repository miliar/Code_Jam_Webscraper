import sys

input = sys.stdin
cases = int(input.readline())

# xor sum
def patrick_sum(value_list):
    size = len(value_list)
    
    if size == 0:
        return 0
    
    result = value_list[0]
    for i in range(1,size):
        result ^= value_list[i]
        
    return result

def sean_sum(value_list):
    return sum(value_list)

for case in xrange (cases):
    total_candies = int(input.readline()) 
    candies = map(int, input.readline().strip().split(" "))
                
    pile_value = -1
    
    # optimizing
    if patrick_sum(candies) == 0:
        candies.sort()
        
        for i in range(total_candies):
            left_sum = patrick_sum(candies[:i+1])
            right_sum = patrick_sum(candies[i+1:])
            
            if (left_sum == right_sum):
                pile_value = sean_sum(candies[i+1:])
                break
            
    if pile_value == -1:
        pile_value = "NO"
        
    print "Case #%d: %s" % (case + 1, str(pile_value))
