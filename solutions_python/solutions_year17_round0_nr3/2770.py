def find_local_best_position(start_index, end_index):
    mid = (end_index + start_index)/2
    mid = max(start_index, mid)
    return mid

def find_global_best_position(n, positions):
    max_of_min_vals = max([ls[0] for ls in positions.values()])
    min_indices = [position for position, ls in positions.iteritems() if ls[0] == max_of_min_vals]
    best_position = min(positions.keys())
    g_max = -1
    for position in min_indices:
        c_max = positions[position][1]
        if c_max > g_max:
            g_max = c_max
            best_position = position

    return best_position

def calculate_answer(N, K):
    best_position = -1
    best_position_min = 0
    best_position_max = 0
    for k in xrange(K):
        empty_stall_start_index = -1
        empty_stall_end_index = -1
        positions = {}
        for i in xrange(1, len(N)):
            if N[i] == '.':
                if empty_stall_start_index == -1:
                    empty_stall_start_index = i
                empty_stall_end_index = i
            else:
                if N[i-1] == '.':
                    position = find_local_best_position(empty_stall_start_index, empty_stall_end_index)
                    ls = position - empty_stall_start_index
                    rs = empty_stall_end_index - position
                    positions[position] = [min(ls, rs), max(ls, rs)]
                empty_stall_start_index = -1

        if positions:
            best_position = find_global_best_position(len(N), positions)
            best_position_min = positions[best_position][0]
            best_position_max = positions[best_position][1]
            N[best_position] = 'o'

    return str(best_position_max) + ' ' + str(best_position_min)

in_f = 'C-small-1-attempt0.in'
out_f = 'C-small-1-attempt0-out.in'
with open(in_f, 'r') as in_file, open(out_f, 'w') as out_file:
    test_cases = int(in_file.readline().strip())
    for t in xrange(1, test_cases + 1):
        n, k = in_file.readline().split(' ')
        N = ['o']
        N.extend(['.' for _ in xrange(int(n))])
        N.append('o')
        K = int(k)
        answer = calculate_answer(N, K)
        out_file.write('Case #' + str(t) + ': ' + answer + '\n')
