import sys
inputs = sys.stdin

def solution(shylevel_counts):
    level_to_count = dict((idx, int(count)) for idx, count in enumerate(shylevel_counts))
    standing = 0
    for shylevel, count in enumerate(shylevel_counts):
        if shylevel == len(shylevel_counts) - 1:
            continue
        standing += int(count)
        nextlevel = shylevel + 1
        if standing < nextlevel:
            level_to_count[shylevel] += (int(nextlevel) - standing)
            standing += level_to_count[shylevel]
    return sum(level_to_count.values()) - sum([int(x) for x in shylevel_counts])

orig_stdout = sys.stdout
output = file('output.out', 'w')
sys.stdout = output

case_count = int(inputs.readline())
for idx in xrange(1, case_count + 1):
    max_shylevel, shylevel_counts = inputs.readline().split()
    result = solution(shylevel_counts)
    print "Case #{}: {}".format(idx, result)

sys.stdout = orig_stdout
output.close()
