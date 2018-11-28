import sys
import re

input_file = sys.argv[1]
lines = open(input_file).read().splitlines()
fp = open(input_file.replace('.in', '.out'), 'w')

num_test_cases = lines.pop(0)
for case, line in enumerate(lines):
    _, shy_counts = line.split(' ')
    num_need = 0
    num_standing = 0
    for i, shy_count in enumerate(shy_counts):
        shy_count = int(shy_count)
        if shy_count > 0:
            while i > num_standing:
                num_need += 1
                num_standing += 1
            num_standing += shy_count
    fp.write('Case #{}: {}\n'.format(case + 1, num_need))
fp.close()
