
def last_tidy_num(n):
    n = list(map(int, list(n)))  # convert digit to the list of INTs
    i = 0  # current key
    while i + 1 != len(n):
        # print i, n[i], n
        if i == 0 and n[i] == 0:  # If we aren't in the beginning and leading el-t is zero
            # print 'case 1'
            del n[i]
        elif n[i + 1] >= n[i]:  # everything is OK, go to the next
            i += 1
        else:
            # Decrease or delete digit here
            #############
            if (i != 0 and n[i] != 0) or (i == 0 and n[i] != 0):  # do only decreasing
                # print 'case 2'
                n[i] -= 1
                n = n[:i + 1] + [9] * (len(n) - i - 1)
            elif i != 0 and n[i] == 0:  # decrease current + update previous digits as well
                # print 'case 3'
                part_of_num = int(''.join([str(digit) for digit in n[:i+1]]))  # convert num to int
                part_of_num = [int(digit) for digit in str(part_of_num - 1)]  # decrease num - 1
                n = part_of_num + [9] * (len(n) - i + 1)
            i = 0
    return ''.join([str(digit) for digit in n])

# print last_tidy_num('879')

# t = 4
# data = ['132', '1000', '7', '111111111111111110']
# n = data[i]
# n, m = [int(s) for s in raw_input().split(" ")]
# if False:
nums = []
with open('B-large.in', 'r') as f:
    for line in f:
        v = line.strip()
        nums.append(v)

# T = int(raw_input())  # read a line with a single integer
# T = int(raw_input())  # read a line with a single integer
results = []
t = int(nums.pop(0))
for i in xrange(t):
    # N = raw_input()
    N = nums[i]
    res = last_tidy_num(N)
    case = i + 1
    text = "Case #{}: {}".format(case, res)
    print text
    results.append(text)

with open('results.out', 'w') as f:
    f.write('\n'.join(results))
