import numpy as np

with open('in.txt') as f:
    lines = f.readlines()
lines = [l.split('\n')[0] for l in lines]
t = int(lines[0])


def count_area(n, k, pstack):
    pstack_s = sorted(pstack, key=lambda x: 2 * x[1] * x[0], reverse=True)
    pstack_r = sorted(pstack, key=lambda x: x[0], reverse=True)
    areas = []
    for pr in pstack_r:
        circle_area = np.pi * pr[0] ** 2
        side_area = 2. * np.pi * pr[0] * pr[1]
        pstack_sr = list(pstack_s)
        pstack_sr.remove(pr)
        for i in xrange(k - 1):
            side_area += 2. * np.pi * pstack_sr[i][0] * pstack_sr[i][1]
        exposed_area = circle_area + side_area
        areas.append(exposed_area)

    return max(areas)


f = open('out.txt', 'w')
line_counter = 1
for i in xrange(1, t + 1):
    n, k = lines[line_counter].split(' ')
    n = int(n)
    k = int(k)
    line_counter += 1
    pstack = []
    for j in xrange(n):
        ri, hi = lines[line_counter].split(' ')
        ri = int(ri)
        hi = int(hi)
        pstack.append((ri, hi))
        line_counter += 1
    print n, k, pstack
    ans = count_area(n, k, pstack)
    print('Case #%s: %f \n' % (i, ans))
    f.write('Case #%s: %f \n' % (i, ans))
