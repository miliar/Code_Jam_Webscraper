import sys

def solve_case(shy_counts):
    extras_needed = 0

    standing = 0
    for shyness, c in enumerate(shy_counts):
        if standing < shyness:
            extras_needed += (shyness - standing)
            standing += (shyness - standing)
        standing += c

    return extras_needed

if __name__ == '__main__':
    fname = sys.argv[1]
    f = open(fname, 'r')
    lines = f.readlines()
    n = int(lines[0])
    for i,line in enumerate(lines[1:]):
        counts = list(int(c) for c in line.strip().split()[1])
        print 'Case #%d: %d' % (i+1, solve_case(counts))
        
