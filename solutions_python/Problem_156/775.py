__author__ = 'Christian'
import sys, math

def analyze_list(l):
    loops = 0

    if not l:
        return 0


    l.sort()
    #print l

    largest = l[-1]
    if largest <= 3:
        return largest

    target_cut_max = int(math.sqrt(largest))

    best_time = largest

    for target_cut in range(2, target_cut_max+1):
        moved_pancakes = largest / target_cut
        new_val = largest - ((target_cut -1) * moved_pancakes)

        new_l = l[:-1] + [new_val] + ((target_cut - 1) * [moved_pancakes])

        potential_time = (target_cut - 1) + analyze_list(new_l)
        #print target_cut, potential_time, best_time, new_l
        if potential_time < best_time:
            best_time = potential_time

    return best_time

# print analyze_list([6, 6, 6, 6, 9, 9])
# print 'expect 8'
# print analyze_list([4, 4, 9, 9])
# print 'expect 7'
# print analyze_list([1, 3, 6, 9])
# print 'expect 6'
# print analyze_list([2, 3, 3, 9, 9, 9])
# print 'expect 8'
# print analyze_list([7,7])
# print 'expect 6'
# print analyze_list([2, 2, 3, 9])
# print 'expect 5'
# print analyze_list([1,2,7])
# print 'expect 5'
# print analyze_list([6,9])
# print 'expect 6'
# print analyze_list([1,9])
# print 'expect 5'
# sys.exit()

#fname = 'test_b.txt'
fname = 'B-small-attempt8.in'
#fname = 'B-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')

N = int(data[0])
data = data[1:]

for i in range(N):
    nums = data[2*i+1].split(' ')
    l = [int(c) for c in nums]

    l2 = [x for x in l if x != 1]


    res = analyze_list(l)
    print >> res_file, 'Case #%s: %s' % (i+1, res)

res_file.close()


