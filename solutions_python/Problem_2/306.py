import sys


def process_file(fp):
    num_cases = int(fp.readline())
    result = []
    for i in range(num_cases):
        res = process_case(fp)
        result.append( "Case #%d: %d %d" % (i+1, res[0], res[1]))
    return '\n'.join(result)

def process_case(fp):
    t_time = int(fp.readline())

    num_a, num_b = map(int, fp.readline().split())
    a_sched = []
    b_sched = []
    a_depts = []
    a_arrivals = []
    b_depts = []
    b_arrivals = []
    for i in range(num_a):
        item = fp.readline().split()
        a_sched.append(item)
        a_depts.append(item[0])
        b_arrivals.append(item[1])

    for i in range(num_b):
        item = fp.readline().split()
        b_sched.append(item)
        b_depts.append(item[0])
        a_arrivals.append(item[1])


    
    res_a = num_a - count_for_station(a_depts, a_arrivals, t_time)
    res_b = num_b - count_for_station(b_depts, b_arrivals, t_time)

#    import pdb;pdb.set_trace()
    return (res_a, res_b)

def count_for_station(depts, arrivals, t_time):
    depts.sort()
    arrivals.sort()
    res = 0
    for dept in depts:
        if not arrivals:
            break
        if minutes(arrivals[0]) + t_time <= minutes(dept):
            res += 1
            arrivals = arrivals[1:]
    return res


def minutes(tstamp):
    hrs,mins = map(int, tstamp.split(':'))
    return hrs*60 + mins

if __name__ == '__main__':
    print process_file(sys.stdin)
