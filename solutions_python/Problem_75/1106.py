import sys

in_file = open(sys.argv[1], 'r')
out_file = open(sys.argv[2], 'w')

def get_answer(s):
    b = s.split(' ')
    combine_num = int(b[0])
    opposed_num = int(b[1 + combine_num])
    combine = {}
    opposed = {}
    for x in xrange(combine_num):
        e = b[1 + x]
        combine[e[0] + e[1]] = e[2]
        combine[e[1] + e[0]] = e[2]
    for x in xrange(opposed_num):
        e = b[1 + combine_num + 1 + x]
        opposed[e[0]] = e[1]
        opposed[e[1]] = e[0]
    elements = b[1 + combine_num + 1 + opposed_num + 1]

    result = []

    for x in elements:
        if result and result[-1] + x in combine:
            result.append(combine[result.pop() + x])
        elif x in opposed and opposed[x] in result:
            result=[]
        else:
            result.append(x)
    return "[" + (', '.join(result)).strip()[:-1] + "]"



n = int(in_file.readline())
for x in xrange(n):
    s = in_file.readline()
    get_answer(s.strip())
    out_file.writelines("Case #%d: %s\n" % (x + 1, get_answer(s)))

