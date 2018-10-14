__author__ = 'Christian'


def analyze_list(counts):

    min_method_1 = 0
    max_diff = None
    current_val = None
    for v in counts:
        if current_val is None:
            current_val = v
        else:
            if v < current_val:
                diff = current_val - v
                min_method_1 += diff
                if max_diff is None or diff > max_diff:
                    max_diff = diff
            current_val = v

    min_method_2 = 0
    if max_diff is not None:
        for v in counts[:-1]:
            if v > max_diff:
                min_method_2 += max_diff
            else:
                min_method_2 += v

    return min_method_1, min_method_2


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
    counts = [int(x) for x in data[2*i+1].split(' ')]

    res = analyze_list(counts)
    print >> res_file, 'Case #%s: %s %s' % (i+1, res[0], res[1])

res_file.close()

