nums = []

with open('B-large.in', 'r') as f:
    T = int(f.readline())
    for i in range(T):
        nums.append(f.readline().strip())

case = 1

with open('B-large.out', 'w') as f:
    for str in nums:
        res = str[-1]
        for i in range(len(str) - 2, -1 , -1):
            if str[i] <= res[0]:
                res = str[i] + res
            else:
                res = chr(ord(str[i]) - 1) + '9' * len(res)
        f.write('Case #%i: %s\n' % (case, res.lstrip('0')))
        case += 1
