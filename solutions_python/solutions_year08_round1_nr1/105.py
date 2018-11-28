import sys, os
##
##file_in = 'A-small-attempt0.in'
##file_out = 'A-small.out'
file_in = 'A-large.in'
file_out = 'A-large.out'
##file_in = 'test.txt'
##file_out = 'test.out.txt'

f = open(file_in, 'r')
res_f = open(file_out, 'w')

def scalar_prod(v1, v2, n):
    s = 0
    for i in range(n):
        s += v1[i]*v2[i]
    return s

def reverse_list(l):
    res_l = []
    for i in l:
        res_l = [i]+res_l
    return res_l

test_cases_num = 0

l = f.readline().strip('\n')
test_cases_num = int(l)
for i in range(test_cases_num):
    l = f.readline().strip('\n')
    n = int(l)
    l = f.readline().strip('\n')
    v1 = [int(x) for x in l.split()]
    l = f.readline().strip('\n')
    v2 = [int(x) for x in l.split()]

    v1.sort()
    v2.sort()
    v2=reverse_list(v2)

    v = scalar_prod(v1, v2, n)
    print >> res_f, "Case #%s: %s" % ((i+1), v)


try:
    f.close()
    res_f.close()
except:
    pass

print "done"