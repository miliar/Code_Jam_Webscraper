problem = 'C'
scale = 'large-2'

infile = problem + '-' + scale + '.in'
outfile = problem + '-' + scale + '.out'

input = open(infile, 'r')
output = open(outfile, 'w')

ncase = int(input.readline().rstrip()) 

fs = []

import itertools
patterns = [(25, "0", 3),
            (1, "1", 2),
            (2, "1", 2),
            (3, "1", 1),
            (4, "1", 1),
            (1, "2", 1)]
for pattern in patterns:
    for digits in itertools.combinations(list(range(0,25)), pattern[0]):
        pre = ["0"]*25
        for digit in digits:
            pre[digit] = pattern[1]
        pre = ''.join(pre)
        pre = str(int(pre))
        if pre == "0": pre = ''
        for m in range(-1, pattern[2]+1):
            if m == -1:
                mid = ''
            else:
                mid = str(m)
            post = pre[::-1]
            if pre == '' and mid == '': continue
            whole = int(pre + mid + post)
            sq = str(whole*whole)
            l = len(sq)
            for j in range(0, l//2):
                if sq[j] != sq[l-1-j]:
                    break
            else:
                fs.append(sq)


def process(input):
    a, b = input.readline().rstrip().split()
    a = int(a)
    b = int(b)
    ct = 0
    for ele in fs:
        v = int(ele)
        if v >= a and v <= b:
            ct += 1
    return str(ct)

for k in range(1, ncase+1):
    result = process(input)
    print(k, result)
    output.write("Case #%d: %s\n" % (k, result))
