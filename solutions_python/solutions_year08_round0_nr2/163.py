INPUT = 'B-large.in'
OUTPUT = INPUT.replace('.in', '.out')

f = open(INPUT, 'r')
input = f.readlines()
f.close()
N = eval(input[0])
input = input[1:]

f = open(OUTPUT, 'w')

def parse_time(t):
    h, m = t.split(':')
    h, m = int(h), int(m)
    return h*60+m

def calc_train(leaves, joins):
    t = range(0, 23*60 + 59)
    current = 0
    needed = 0
    for i in xrange(len(t)):
        if i in joins:
            current += joins.count(i)
        if i in leaves:
            current -= leaves.count(i)
            needed = min(current, needed)
    return abs(needed)
        

case = 0
i = 0
while case < N:
    case += 1
    t = eval(input[i].strip())
    i += 1
    na, nb = input[i].strip().split(' ')
    na, nb = eval(na), eval(nb)
    i += 1
    leave_a = []
    leave_b = []
    join_a = []
    join_b = []
    la = []
    lb = []
    ja = []
    jb = []
    for j in xrange(na):
        tmp1, tmp2 = input[i + j].strip().split(' ')
        la.append(tmp1)
        jb.append(tmp2)
        tmp1, tmp2 = parse_time(tmp1), parse_time(tmp2)
        leave_a.append(tmp1)
        join_b.append(tmp2 + t)
    i += na
    for j in xrange(nb):
        tmp1, tmp2 = input[i + j].strip().split(' ')
        lb.append(tmp1)
        ja.append(tmp2)
        tmp1, tmp2 = parse_time(tmp1), parse_time(tmp2)
        leave_b.append(tmp1)
        join_a.append(tmp2 + t)
    i += nb
    trains = []
    trains.append(calc_train(leave_a, join_a))
    trains.append(calc_train(leave_b, join_b))
    f.write('Case #%d: %d %d\n' % (case, trains[0], trains[1]))
#    print 'Case %d: %d %d, time = %d, na %d, nb %d' % (case, trains[0], trains[1], t, na, nb)
#   print 'leave a ', la
#    print 'join a ', ja
#    print 'leave b ', lb
#    print 'join b ', jb
f.close()
