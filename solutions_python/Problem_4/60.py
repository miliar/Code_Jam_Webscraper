INPUT = 'A-large.in'
OUTPUT = INPUT.replace('.in', '.out')

f = open(INPUT, 'r')
input = f.readlines()
f.close()
N = eval(input[0])
input = input[1:]

f = open(OUTPUT, 'w')

case = 0
i = 0
while case < N:
    case += 1
    l = eval(input[i].strip()) # length of vectors
    i += 1
    v1 = input[i].strip().split(' ')
    i += 1
    v2 = input[i].strip().split(' ')
    i += 1
    for j in xrange(l):
        v1[j] = eval(v1[j])
        v2[j] = eval(v2[j])
    v1.sort()
    v2.sort()
    v2.reverse()
    s = 0
    for j in xrange(l):
        s += v1[j] * v2[j]
#    print 'Case #%d: %d' % (case, s)
    f.write('Case #%d: %d\n' % (case, s))
    
f.close()
