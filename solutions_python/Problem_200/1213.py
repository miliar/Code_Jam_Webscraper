import sys

lines = open(sys.argv[1], "r").read().splitlines()
res = ""

cases = int(lines[0])
idx = 1

for c in xrange(cases):
    num = int(lines[c+1])
    num_digit_l = list(str(num))[::-1]
    for i in xrange(len(num_digit_l)-1):
        if int(num_digit_l[i+1]) > int(num_digit_l[i]):
            num = num - (num % 10**(i+1) + 1)
            num_digit_l = list(str(num))[::-1]
    res += "Case #%d: %d\n" %(c+1, num)
open(sys.argv[2], "w").write(res)
