import itertools
from codejam import CodeJam

cj = CodeJam(debug=False)

for case in cj.cases:
    elements = cj.get_int()
    v1 = map(int, cj.get_lines(1)[0].split(' '))
    v2 = map(int, cj.get_lines(1)[0].split(' '))
    total = 0

    if max(v1) > max(v2):
        v1.sort(reverse=True)
        v2.sort()
    else:
        v2.sort(reverse=True)
        v1.sort()

    for i in xrange(elements):
        total += v1[i] * v2[i]

    print total
    cj.write_case(total)
