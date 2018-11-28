import sys

if __name__ == '__main__':
    filename = sys.argv[1]   
    f = open(filename)
    cases = int(f.readline().strip())
    for n in xrange(1,cases+1):
        numbers = [ int(a) for a in f.readline().strip().split() ]
        result = 0
        threshold = 3*numbers[2] - 2
        surprise_threshold = 3*numbers[2] - 4
        if surprise_threshold < 0:
            surprise_threshold = 1 
        surprise_count = 0
        for tp in numbers[3:]:
            if tp >= threshold:
                result += 1
            elif surprise_count < numbers[1] and \
                tp >= surprise_threshold:
                result += 1
                surprise_count += 1
        print 'Case #%d:'%n, result

