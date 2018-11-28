import pdb

input_file = 'B-large.in'
input = open(input_file)
lines = input.readlines()
input.close()


def trim(list_num):
    for i, digit in enumerate(list_num):
        if digit != '0':
            return ''.join(list_num[i:])


def solve(num):
    # last non-increasing index
    num = list(num)
    n = len(num)
    lni = 0
    prev = num[0]
    for i, cur in enumerate(num[1:]):
        if cur > prev:
            lni = i + 1
        elif cur < prev:
            list_num = num[0:lni] + [str(int(num[i]) - 1)] + (n-lni-1)*['9']
            return trim(list_num)
        prev = cur
    return ''.join(num)


output_file = 'B-large.out'
output = open(output_file, 'wb')
for i, line in enumerate(lines[1:]):
    num = line.strip()
    ans = solve(num)
    output.write('Case #{i}: {ans}\n'.format(i=i+1, ans=ans))
output.close()
