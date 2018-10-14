import sys

def scalar_prod(a, b):
    return sum(i*j for i,j in zip(a,b))


in_file = file(sys.argv[1], 'r')

num_cases = int(in_file.readline())

for case in range(1, num_cases + 1):
    n = int(in_file.readline())
    a = map(int, in_file.readline().split())
    b = map(int, in_file.readline().split())

    b.sort()
    a.sort()
    a.reverse()
    
    print 'Case #%d: %d' % (case, scalar_prod(a,b))

