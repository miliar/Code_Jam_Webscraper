import math

input_file = 'C-small-attempt3.in'
output_file = 'C-small-attempt3.out'

# Prepare output to file
open(output_file, 'w').write('')
def print_to_file(line):
    open(output_file, 'a').write(line + '\n')

# Read input
lines = [line.strip() for line in open(input_file, 'r')]

# First element is just the number of games
lines.pop(0)

count = 0
for line in lines:
    count += 1
    result_count = 0
    line = line.split(' ')
    min = int(line[0])
    max = int(line[1])
    for i in range(int(math.floor(math.sqrt(min))),max+1):
        if str(i) == str(i)[::-1]:
            i2 = i*i
            if (min <= i2 <= max) and (str(i2) == str(i2)[::-1]):
                result_count += 1
    print_to_file('Case #' + str(count) + ': ' + str(result_count))
                
