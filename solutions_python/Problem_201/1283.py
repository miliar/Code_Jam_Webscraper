"""

"""

import sys

def seat_visitor(n):

    if n & 0x1:
        # n is odd
        return n // 2, n // 2, n // 2, n // 2
    else:
        # n is even
        return n // 2, n // 2 - 1, n // 2 - 1, n // 2


with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    test_cases = [(int(n), int(k)) for n, k in [s[:-1].split() for s in f.readlines()]]

personal_space = []
for stall_size, n_visitors in test_cases:
    stall_sizes = {stall_size:1}
    max_space, min_space = None, None
    for _ in range(n_visitors):
        largest_stall_range = max(stall_sizes.keys())

        stall_sizes[largest_stall_range] -= 1
        if stall_sizes[largest_stall_range] == 0:
            stall_sizes.pop(largest_stall_range)

        max_space, min_space, left_stall_size, right_stall_size = seat_visitor(largest_stall_range)

        if left_stall_size in stall_sizes:
            stall_sizes[left_stall_size] += 1
        else:
            stall_sizes[left_stall_size] = 1

        if right_stall_size in stall_sizes:
            stall_sizes[right_stall_size] += 1
        else:
            stall_sizes[right_stall_size] = 1

    personal_space.append((max_space, min_space))

t = 1
with open(sys.argv[2], 'w') as f:
    for space_to_left, space_to_right in personal_space:
        f.write("Case #%d: %d %d\n" % (t, space_to_left, space_to_right))
        t += 1
