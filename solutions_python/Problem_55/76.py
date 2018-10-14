input_file = 'input_large'
import sys,copy
fp = open(input_file);
case_num = int(fp.readline())
for i in range(0, case_num):
    R, k, N = [int(x) for x in fp.readline().split()]
    groups = [int(x) for x in fp.readline().split()]
    d = {} 
    l = []
    count = 0
    offset = 0
    while True:
        sub_total = 0
        sub_count = 0
        c = copy.copy(groups)
        c_str =' '.join((str(x) for x in c)) 
        if c_str in d:
            offset = d[c_str]
            break
        else:
            d[c_str] = count 
        while sub_total + groups[0] <= k and sub_count < N:
            num = groups[0]
            del groups[0]
            groups.append(num)
            sub_total += num
            sub_count += 1
        l.append(sub_total)
        count += 1
    cycle = l[offset:]

    if R < offset:
        print 'Case #%d: %d' % (i + 1, sum(l[:R])) 
    else:
        rep = (R - offset) / len(cycle)
        total = rep * sum(cycle) + sum(cycle[:((R - offset) % len(cycle))]) + sum(l[:offset])
        print 'Case #%d: %d' % (i + 1, total)
