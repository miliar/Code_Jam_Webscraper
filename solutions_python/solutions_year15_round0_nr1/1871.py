import sys

def compute(levels):
    total_extra = 0
    standing = 0
    for level, count in enumerate(levels):
        extra = max(0, level - standing)
        standing += int(count) + extra
        total_extra += extra
    return total_extra

def main(args):
    afile = open(args[0]).readlines()
    for i, line in enumerate(afile[1:], 1):
        line = line.strip()
        print ("Case #%s: %d" % (i, compute(line.split()[1])))

main(sys.argv[1:])
