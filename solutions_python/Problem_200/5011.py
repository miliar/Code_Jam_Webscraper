import sys

def last_tidy(num):
    for i in xrange(num, 0, -1):
        if is_tidy(i):
            return i

def is_tidy(num):
    digits = list(str(num))
    return sorted(digits) == digits

lines = sys.stdin.readlines()
inputs = [int(line.strip()) for line in lines[1:] if line]

for num, input in enumerate(inputs):
    print 'Case #%d: %d' % (num + 1, last_tidy(input))
