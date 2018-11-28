
def apply_one_round (k, list_of_group_sizes):
    # apply just one round on the rollercoaster and
    # returns the money earned and new state of queue
    s1= sum (list_of_group_sizes)
    if s1 <= k:
        return s1, list_of_group_sizes
    s = 0
    i = 0
    while s+list_of_group_sizes[i] <= k:
        s += list_of_group_sizes[i]
        i += 1
    return s, list_of_group_sizes[i:] + list_of_group_sizes[:i]

def apply_N_rounds (k, list_of_group_sizes):
    # applies enough number of rounds on the roller coaster
    # until state of queue must repeat itself
    # returns a list of queue state and money earned after every round applied
    N = len(list_of_group_sizes)
    states = []
    money_earned_so_far = 0
    current_round = 0

    for curr_round in range(N+10):
        states.append((money_earned_so_far, tuple(list_of_group_sizes)))
        curr_money, list_of_group_sizes = apply_one_round (k, list_of_group_sizes)
        money_earned_so_far += curr_money

    return states


def simulate_all_rounds (R, k, list_of_group_sizes):
    # make an efficient simulation of running the coaster R times
    N = len(list_of_group_sizes)
    states = apply_N_rounds (k, list_of_group_sizes)
    if R <= len(states)-1:
        return states[R][0]
    else:
        last_reached_queue_state =states[-1][1]
        i = len(states)-2
        while states[i][1] != last_reached_queue_state:
            i -=1
        len_of_repeating_cycle = len(states)-1-i
        money_through_cycle = states[-1][0] - states[i][0]
        n_cycles = (R-i) // len_of_repeating_cycle
        money_earned_so_far = states[i][0] + n_cycles*money_through_cycle
        last_round_reached = i + n_cycles*len_of_repeating_cycle
        more_rounds_needed = R - last_round_reached
        assert more_rounds_needed >=0
        list_of_group_sizes = states[-1][1]
        for i in range (more_rounds_needed):
            curr_money, list_of_group_sizes = apply_one_round (k, list_of_group_sizes)
            money_earned_so_far += curr_money
        return money_earned_so_far
    


    
f_in = open('c:/temp/codejam/qualification/C-large.in')
f_out = open('c:/temp/codejam/qualification/C-large.out','w')

T = int(f_in.readline())
for case in range(T):
    R, k, N = [int(x) for x in f_in.readline().split()]
    list_of_group_sizes = [int(x) for x in f_in.readline().split()]
    res = simulate_all_rounds (R,k, list_of_group_sizes)
    f_out.write('Case #' + str(case+1) + ': ' + str(res) + '\n')

f_in.close()
f_out.close()

