__author__ = 'Christian'

def analyze_list(l):

    current_count = 0
    added_friends = 0
    print l

    for index, count in enumerate(l):
        #print index, count, current_count, added_friends
        if count == 0:
            continue
        if index <= current_count:
            current_count += count
        else:
            added_friends += (index - current_count)
            current_count = index + count

    return added_friends

#fname = 'test_a.txt'
#fname = 'A-small-attempt0.in'
fname = 'A-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')

N = int(data[0])
data = data[1:]

for i in range(N):
    Smax, nums = data[i].split(' ')
    Smax = int(Smax)
    l = [int(c) for c in nums]

    res = analyze_list(l)
    print >> res_file, 'Case #%s: %s' % (i+1, res)

res_file.close()


