__author__ = 'Christian'

#fname = 'test_c.txt'
#fname = 'C-small-1-attempt0.in'
#fname = 'C-small-2-attempt0.in'
fname = 'C-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')

def split_interval(n):
    if n <= 1:
        return 0L, 0L
    elif n == 2:
        return 1L, 0L
    elif n % 2 == 1:
        return (n-1)/2, (n-1)/2
    else:
        return n/2, n/2-1

def compute_stall(N, K):
    current_stall_situation = {N : 1}
    current_stall_available_intervals = [N]

    people_left = K

    while people_left:
        current_interval = current_stall_available_intervals.pop(0)
        spots_in_that_interval = current_stall_situation[current_interval]
        n1, n2 = split_interval(current_interval)
        #print people_left, current_interval, spots_in_that_interval, n1, n2
        if people_left <= spots_in_that_interval:
            return n1, n2
        if n1 == n2:
            if n1 in current_stall_available_intervals:
                current_stall_situation[n1] += 2*spots_in_that_interval
            else:
                current_stall_available_intervals.append(n1)
                current_stall_situation[n1] = 2 * spots_in_that_interval
        else:
            if n1 in current_stall_available_intervals:
                current_stall_situation[n1] += spots_in_that_interval
            else:
                current_stall_available_intervals.append(n1)
                current_stall_situation[n1] = spots_in_that_interval
            if n2 in current_stall_available_intervals:
                current_stall_situation[n2] += spots_in_that_interval
            else:
                current_stall_available_intervals.append(n2)
                current_stall_situation[n2] = spots_in_that_interval
        people_left -= spots_in_that_interval


T = int(data[0])
for i in range(T):
    N, K = data[i+1].split(' ')
    n1, n2 = compute_stall(long(N), long(K))
    print >> res_file, "Case #%s: %s %s" % (i+1, n1, n2)

res_file.close()