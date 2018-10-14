import sys, bisect

filename, extension = sys.argv[1].split('.')
assert(extension=='in')
src = open(sys.argv[1])
result = open(filename + '.out', 'wb')

num_tests = int(src.readline().rstrip())
#
# def solve(D, horses):
#     max_time = max((D-horse[0])/horse[1] for horse in horses)
#     return D / max_time

for test_idx in range(1,num_tests+1):
    D, N = [int(each) for each in src.readline().split(' ')]
    lowest_time = 0
    for _ in range(N):
        coord, speed = [float(each) for each in src.readline().split(' ')]
        time = (D - coord)/ speed
        if time > lowest_time:
            lowest_time = time
    # print 'CASE D=%s, horses=%s' %(D, horses)
    solution = '{0:.6f}'.format(D / lowest_time)
    # print 'Solution:', solution
    result.write('Case #{}: {}\n'.format(test_idx, solution) )
