from collections import Counter
from math import ceil
from math import floor


input_file = open("c_small_input.txt", "r")
output_file = open("c_small_output.txt", "w")
data = input_file.readlines()
T = int(data[0])
for t in range(1, T+1):
    N, K = [int(x) for x in data[t].split()]
    counts = Counter()
    counts[N] += 1
    for i in range(K-1):
        to_split = max(counts)
        counts[to_split] -= 1
        #To prevent ridiculousness from occuring.
        if counts[to_split] <= 0:
            counts.pop(to_split, None)
        counts[ceil((to_split -1)/2)] += 1
        counts[floor((to_split -1)/2)] += 1
    #Now calculate what happens for the last person.
    chosen_area = max(counts)
    maximum = ceil((chosen_area - 1)/2)
    minimum = floor((chosen_area - 1)/2)
    output_file.write("Case #{}: {} {}\n".format(t, maximum, minimum))
    
            
    


#output_file.write("Case #{}: {}\n".format(t, tidy))
input_file.close()
output_file.close()
print("Files closed")
