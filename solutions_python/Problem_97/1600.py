import sys

def find_recycled_numbers(start, stop):
    current, count = start, 0
    pairs = []
    while current <= stop:
        currstr = str(current)
        for i in xrange(1, len(currstr)):
            prefix, suffix = currstr[:i], currstr[i:]
            recycledstr = suffix + prefix
            recycled = int(recycledstr)
            if len(recycledstr) == len(currstr) and start <= recycled <= stop and recycled > current:
                pairs.append((current, recycled))
        current += 1
    return len(set(pairs))

if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename) as f:
        lines = map(str.strip, f.readlines())
        for i, line in enumerate(lines[1:]):
            start, stop = map(int, line.split())
            print "Case #%s: %s" % (i + 1, find_recycled_numbers(start, stop))