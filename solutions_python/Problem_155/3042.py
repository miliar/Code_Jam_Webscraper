#!/usr/local/bin/python
import string
import sys

sample_input = [line.strip() for line in open('A-large.in')]
test_count = int(sample_input[0])
cases = sample_input[1::]

for i in range(0, test_count):
    cur_case = string.split(cases[i])
    max_shyness_level = int(cur_case[0])
    
    ans = 0
    total = 0

    audience = list(cur_case[1])
    for j in range(0, len(audience)):
        if (total > max_shyness_level):
            break
        else:
            cur_shyness_count = int(audience[j])

            extras = j - total
            if (extras > 0):
                ans = ans + extras
                total = total + extras
            
            total = total + cur_shyness_count

    print('Case #{0}: {1}'.format(i + 1, ans))
