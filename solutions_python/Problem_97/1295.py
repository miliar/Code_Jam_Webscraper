import sys

def cycle_by(text, offset):
    return text[offset:] + text[:offset]

def cycled_digits_of(n):
    text = str(n)
    for i in xrange(1, len(text)):
        cycle = cycle_by(text, i)
        if cycle[0] != '0':
            yield int(cycle)

def count_recycled_pairs(low, high):
    count = 0
    cycled = set()
    for i in xrange(low, high + 1):
        for cycle in cycled_digits_of(i):
            if i != cycle and cycle >= low and cycle <= high:
                # print "{0}, {1}".format(i, cycle)
                cycled.add((i, cycle))
    return len(cycled) / 2

sys.stdin.next() # skip count line
for i, line in enumerate(sys.stdin):
    low, high = map(int, line.split(' '))
    print "Case #{0}: {1}".format(i + 1, count_recycled_pairs(low, high))
