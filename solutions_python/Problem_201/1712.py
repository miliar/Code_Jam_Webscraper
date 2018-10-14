import re
import math

def bathroom(filename):
    with open(filename, 'r') as f:
        numTests = f.readline()
        output = open('stall_out.txt', 'w')
        for idx in range(1, int(numTests)+1):
            line = re.split(' ', f.readline())
            N = int(line[0])
            k = int(line[1])

            print N, k

            h = math.floor(math.log(k,2))

            num_leaves = 2**h

            remainder = k - (num_leaves-1)

            largest_parent = math.floor(N/(2**(h-1)))
            b = (largest_parent-1)/2
            a = largest_parent - 1 -b

            c = 0
            d = 0

            if a==b:
                c = a
                d = b-1
            else:
                c=b
                d = b

            num_large_numbers = N - d * num_leaves - (num_leaves - 1)

            parent = 0

            if remainder <= num_large_numbers:
                parent = a
            else:
                parent = d

            result_min = (parent - 1)/2
            result_max = parent - 1 - result_min

            output.write('Case #%d: %d %d\n' % (idx, result_max, result_min))

bathroom('C-small-1-attempt0.in.txt')
