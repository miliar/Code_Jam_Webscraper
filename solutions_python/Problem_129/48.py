# Justin Ghan <justin.ghan@gmail.com>

f_in = open('A-small-attempt0.in', 'r')
f_out = open('A-small-attempt0.out', 'w')

def calculate_cost(N, n):
    return n * (2 * N - n + 1) / 2

num_cases = int(f_in.readline().strip())

for idx_case in range(num_cases):
    N, M = [int(s) for s in f_in.readline().strip().split()]
    stop_set = set()
    on_dict = {}
    off_dict = {}
    cost1 = 0
    for i in range(M):
        oi, ei, pi = [int(s) for s in f_in.readline().strip().split()]
        stop_set.add(oi)
        stop_set.add(ei)
        if oi not in on_dict.keys():
            on_dict[oi] = 0
            off_dict[oi] = 0
        if ei not in on_dict.keys():
            on_dict[ei] = 0
            off_dict[ei] = 0
        on_dict[oi] += pi
        off_dict[ei] += pi
        cost1 += pi * calculate_cost(N, ei - oi)
    
    stop_list = sorted(list(stop_set))
    pass_dict = {}
    cost2 = 0
    for idx_current_stop in range(len(stop_list)):
        currrent_stop = stop_list[idx_current_stop]
        pass_dict[currrent_stop] = on_dict[currrent_stop]
        if off_dict[currrent_stop] > 0:
            for idx_stop in range(idx_current_stop, -1, -1):
                stop = stop_list[idx_stop]
                if pass_dict[stop] > off_dict[currrent_stop]:
                    pass_dict[stop] -= off_dict[currrent_stop]
                    cost2 += off_dict[currrent_stop] * calculate_cost(N, currrent_stop - stop)
                    off_dict[currrent_stop] = 0
                    break
                else:
                    off_dict[currrent_stop] -= pass_dict[stop]
                    cost2 += pass_dict[stop] * calculate_cost(N, currrent_stop - stop)
                    pass_dict[stop] = 0
    
    f_out.write('Case #{}: {}\n'.format(idx_case+1, cost1 - cost2))

f_in.close()
f_out.close()