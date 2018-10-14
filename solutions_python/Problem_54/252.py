import os
import string

def GCD(a, b):
    if b == 0:
        return a
    
    return GCD(b, a % b)

def FindOptimumAnniversary(event_times):
    event_times.sort()
    
    n = len(event_times)
    
    adjacent_diffs = []
    
    for i in range(0, n - 1):
        adjacent_diffs.append(event_times[i + 1] - event_times[i])
    
    max_factor = adjacent_diffs[0]
    for j in range(0, len(adjacent_diffs)):
        max_factor = GCD(max_factor, adjacent_diffs[j])
        
    minimum_multiples = event_times[0] / max_factor
    is_rounded = (event_times[0] % max_factor) > 0
    if (is_rounded):
        minimum_multiples += 1
        
    return minimum_multiples * max_factor - event_times[0]

if __name__=="__main__":
    input_file = open("large_b.in", 'r')
    output_file = open("large_b.out", 'w')
    
    c = string.atoi(input_file.readline(), 10)
    
    for i in range(1, c + 1):
        line = input_file.readline()
        item_list = line.split(' ')
        n = string.atoi(item_list[0])
        event_times = []
        for j in range(0, n):
            event_times.append(string.atoi(item_list[j + 1]))
            
        output_file.write("Case #" + str(i) + ": " + str(FindOptimumAnniversary(event_times)) + "\n")
        
        
        
        