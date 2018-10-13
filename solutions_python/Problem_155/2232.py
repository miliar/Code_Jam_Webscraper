def min_to_add(s_max, s_arr):
    max_gap = 0
    running_sum = 0

    for i, s in enumerate(s_arr):
        max_gap = max(max_gap, i - running_sum)
        running_sum += s

    return max_gap

def main():
    t = int(raw_input())
    for i in xrange(t):
        line = raw_input()
        line_split = line.split(' ')
        s_max = int(line_split[0])
        s_arr = (int(c) for c in line_split[1])

        print 'Case #{0}: {1}'.format(i + 1, min_to_add(s_max, s_arr))

if __name__ == '__main__':
    main()
