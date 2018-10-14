import sys
from collections import defaultdict


def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    i = 1
    while i <= test_case_count:
        num = content[i]
        num_len = len(num)
        res = num
        if num_len > 1:
            desc_position = None
            for n in xrange(1, num_len):
                if num[n] < num [n - 1]:
                    desc_position = n
                    break
            if desc_position:
                pos = desc_position - 1
                new_nums = []
                #print(new_nums, pos)
                while pos >= 0:
                    new_pos = int(num[pos]) - 1
                    #print(new_pos, pos)
                    if pos == 0:
                        if new_pos <= 0:
                            new_pos = ''
                        new_nums.append(str(new_pos))
                        # print("!!", new_pos)
                        #pos -= 1
                        break
                    else:
                        if new_pos < int(num[pos - 1]):
                            new_pos = '9'
                            pos -= 1
                        else:
                            new_nums.append(str(new_pos))
                            break
                    new_nums.append(str(new_pos))
                #print(new_nums, pos)
                res = num[:pos] + ''.join(new_nums[::-1]) + ('9' * (num_len - desc_position))

        print("Case #%s: %s" % (i, res))
        i += 1

filename = sys.argv[1]
print_solutions(filename)
