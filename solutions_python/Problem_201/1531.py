import sys
import numpy as np

def find_min_max_stalls(n, k):
    levels = int(np.floor(np.log2(k)))
    ind = k - 2**levels
    start_width = n
    if levels == 0:
        max_val = int(np.ceil((start_width - 1) * 0.5))
        min_val = int(np.floor((start_width - 1) * 0.5))
    else:
        directions = bin(ind)[2:].zfill(levels)[::-1]
        for d in directions:
            if d == '0':
                start_width = np.ceil((start_width-1)*0.5)
            else:
                start_width = np.floor((start_width-1)*0.5)
        max_val = int(np.ceil((start_width - 1)*0.5))
        min_val = int(np.floor((start_width - 1)*0.5))
    return max_val, min_val

f = open(sys.argv[1], 'r')
input_file = f.read().splitlines()
f.close()
output_file = open('output_small_2_bathroom_stalls.out', 'w')
t = int(input_file[0])
for i in xrange(1, t + 1):
  n, k = [int(s) for s in input_file[i].split(" ")]
  max1, min1 = find_min_max_stalls(n, k)
  out_string = "Case #" + str(i) + ": " + str(max1) + ' ' + str(min1)
  output_file.write(out_string)
  output_file.write('\n')

# print find_min_max_stalls(3421, 6)