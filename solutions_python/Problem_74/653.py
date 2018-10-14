def time_to_finish_sequence(sequence):
    times = {'O': 0, 'B': 0}
    pos = {'O': 1, 'B': 1}
    time = 0
    for bot,but in sequence:
        p = pos[bot]
        t = times[bot]
        d = abs(but - p)
        required = d
        time = max(t+required, time) + 1
        times[bot] = time
        pos[bot] = but
    return time

def solve(case):
    case = case.split()[1:]
    seq = zip(case[::2], map(int, case[1::2]))
    return time_to_finish_sequence(seq)

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(1, n+1):
        case = raw_input()
        print "Case #%d: %d" % (i, solve(case))

