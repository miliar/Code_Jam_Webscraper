# n, s, engines, queries
# Usage:
# python search.py > out.txt
f = None

def DoCase(n):
    turn_time = int(f.readline())

    na_nb = (f.readline()).split()
    # From a to b:
    n_a_to_b = int(na_nb[0])
    n_b_to_a = int(na_nb[1])

    dep_from_a = []
    arr_to_b = []
    # a -> b:
    for i in range(n_a_to_b):
        times = (f.readline()).split()
        dep = TimeToMins(times[0])
        arr = TimeToMins(times[1])
        dep_from_a.append(dep)
        arr_to_b.append(arr)
    '''
    print 'A -> B:'
    print 'deps:', dep_from_a
    print 'arrs:', arr_to_b
    '''
    dep_from_b = []
    arr_to_a = []
    # b -> a:
    for i in range(n_b_to_a):
        times = (f.readline()).split()
        dep = TimeToMins(times[0])
        arr = TimeToMins(times[1])
        dep_from_b.append(dep)
        arr_to_a.append(arr)
    '''
    print '\nB -> A:'
    print dep_from_b
    print arr_to_a
    '''
    # A:
    dep_from_a.sort()
    arr_to_a.sort()
    # shift arrival times by turnaround
    arr_to_a = map(lambda (x): x + turn_time, arr_to_a)

    # B:
    dep_from_b.sort()
    arr_to_b.sort()
    # shift arrival times by turnaround
    arr_to_b = map(lambda (x): x + turn_time, arr_to_b)

    start_a = CalcStartTrains(arr_to_a, dep_from_a)
    start_b = CalcStartTrains(arr_to_b, dep_from_b)
    print 'Case #%d: %d %d' % (n, start_a, start_b)

def CalcStartTrains(arr_to_a, dep_from_a):
    start_trains = 0
    cur_trains = 0
    while arr_to_a or dep_from_a:
        if not dep_from_a:
            cur_trains += 1
            arr_to_a = arr_to_a[1:]
        elif not arr_to_a:
            if cur_trains > 0:
                cur_trains -= 1
            else:
                start_trains += 1
            dep_from_a = dep_from_a[1:]
        elif arr_to_a[0] <= dep_from_a[0]:
            cur_trains += 1
            arr_to_a = arr_to_a[1:]
        else:
            if cur_trains > 0:
                cur_trains -= 1
            else:
                start_trains += 1
            dep_from_a = dep_from_a[1:]
    return start_trains

def TimeToMins(hh_mm):
    hh = int(hh_mm.split(':')[0])
    mm = int(hh_mm.split(':')[1])
    result = 60 * hh + mm
    #print hh_mm, '->', result
    return result

def main():
    global f
    f = file('in.txt', 'r')
    line = f.readline()
    for i in range(int(line)):
        DoCase(i + 1)

if __name__ == '__main__':
    main()
    


