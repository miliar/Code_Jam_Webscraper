import sys
import math
import heapq # only used for last_bathroom_stall_choice simulation implementation to verify the fast_last_bathroom_stall_choice method


def get_Ls_Rs_max_min(empty_stretch_length):
    floor_half_empty_stretch_length = empty_stretch_length / 2
    if empty_stretch_length % 2 == 0:
        return (floor_half_empty_stretch_length, floor_half_empty_stretch_length - 1)
    return (floor_half_empty_stretch_length, floor_half_empty_stretch_length)

# O(lgN)
def fast_last_bathroom_stall_choice(N, k):
    current_state = get_Ls_Rs_max_min(N)
    total_occupied = 1
    Ls_Rs_max_min_transition_tracker = [[current_state, 1]]

    while total_occupied < k:
        next_state_tracker = []
        incomplete_next_state = None

        for current_state, occupied in Ls_Rs_max_min_transition_tracker:
            Ls, Rs = current_state
            next_L_state = get_Ls_Rs_max_min(Ls)
            if incomplete_next_state is None:
                incomplete_next_state = [next_L_state, occupied]
            elif next_L_state == incomplete_next_state[0]:
                incomplete_next_state[1] += occupied

            next_R_state = get_Ls_Rs_max_min(Rs)
            if next_R_state == incomplete_next_state[0]:
                incomplete_next_state[1] += occupied
            else:
                next_state_tracker.append(incomplete_next_state)
                total_occupied += incomplete_next_state[1]
                if total_occupied >= k:
                    return incomplete_next_state[0]
                incomplete_next_state = [next_R_state, occupied]

        next_state_tracker.append(incomplete_next_state)
        total_occupied += incomplete_next_state[1]
        Ls_Rs_max_min_transition_tracker = next_state_tracker

    return Ls_Rs_max_min_transition_tracker[-1][0]

# O(nlgn), definitely correct--simulates bathroom occupation. Used to verfy the above fast method
def last_bathroom_stall_choice(N, k):
    # Each empty stall interval is stored as (-(R - L), (L, R)),
    # where R and L are indices in the bathroom stall array (0 indexed), and
    # S = L + (R - L)/2
    # Ls = S - L - 1
    # Rs = R - S - 1

    # Initial state:
    h = []
    heapq.heappush(h, (-N, (0, N + 1)))

    min_Ls_Rs = 0
    max_Ls_Rs = 0
    while k > 0:
        # Check if there's a tie for largest stretch of empty stalls
        # In case of tie, take the leftmost one
        largest_empty_stretch = heapq.heappop(h)
        if len(h) > 0:
            next_largest_empty_stretch = h[0]

            if largest_empty_stretch[0] == next_largest_empty_stretch[0]:
                if next_largest_empty_stretch[1][0] < largest_empty_stretch[1][0]:
                    next_largest_empty_stretch = heapq.heappop(h)
                    heapq.heappush(h, largest_empty_stretch)
                    largest_empty_stretch = next_largest_empty_stretch

        # Person should occupy the middle of the largest stretch of empty stalls:
        L, R = largest_empty_stretch[1]
        neg_stretch_length = largest_empty_stretch[0]
        S = L - neg_stretch_length/2
        Ls = S - L - 1
        Rs = R - S - 1
        min_Ls_Rs, max_Ls_Rs = min(Ls, Rs), max(Rs, Ls)

        # Occupy S, and update new created intervals to the heap:
        if Ls > 0:
            heapq.heappush(h, (-Ls, (L, S)))
        if Rs > 0:
            heapq.heappush(h, (-Rs, (S, R)))

        k -= 1

    return max_Ls_Rs, min_Ls_Rs



if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '_output.txt'
    with open(input_file, 'rb') as f:
        with open(output_file, 'wb') as o:
            T = f.readline()
            for i, line in enumerate(f):
                N, k = line.rstrip().split(' ')
                y, z = fast_last_bathroom_stall_choice(int(N), int(k))
                o.write("Case #" + str(i + 1) + ": " + str(y) + ' ' + str(z) + "\n")