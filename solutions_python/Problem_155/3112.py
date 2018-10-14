import sys


raw_in = iter(sys.stdin.readlines())

t = int(next(raw_in))

for case in range(t):
    case_raw = next(raw_in)
    s_max, s_counts = case_raw.split(' ')
    s_max = int(s_max)

    num_required = 0  # the amount required at the current index
    num_available = 0
    for i in range(s_max + 1):
        s_at_count = int(s_counts[i])
        if num_available < i:
            num_required += i - num_available
            num_available = i
        num_available += s_at_count
    print("Case #{0}: {1}".format(
        case + 1, num_required
    ))
