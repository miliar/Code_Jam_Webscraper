import heapq
f = open('C-small-2-attempt1.in')

c = int(f.readline())

result = []

for case in range(c):
    ipt = f.readline().rstrip()
    ipt = ipt.split()
    stalls = int(ipt[0])
    people = int(ipt[1])

    # if stalls == people:
    #     result.append('Case #' + str(case + 1) + ': ' + str(0) + ' ' + str(0) + '\n')
    #     continue
    # elif stalls == people + 1:
    #     result.append('Case #' + str(case + 1) + ': ' + str(1) + ' ' + str(min_v) + '\n')

    # occupied = [-1, stalls]
    gap = [-stalls]
    heapq._heapify_max(gap)
    for i in range(people):
        # gap = []
        # for i in range(len(occupied) - 1):
        #     gap.append(occupied[i + 1] - occupied[i] - 1)

        max_gap = -heapq.heappop(gap)
        # min_gaps = map(lambda x: min_gap == x, gap)
        # selected_gap_index = gap.index(max_gap)

        # strock = max_gap // 2 if max_gap % 2 == 0 else max_gap // 2 + 1

        # stall_index = occupied[selected_gap_index] + strock
        # occupied.insert(selected_gap_index + 1, stall_index)

        min_v = (max_gap - 1) // 2
        max_v = min_v if max_gap % 2 == 1 else min_v + 1
        heapq.heappush(gap, -min_v)
        heapq.heappush(gap, -max_v)
        # gap[selected_gap_index] = min_v
        # gap.insert(selected_gap_index + 1, max_v)

        if i == people - 1:
            result.append('Case #' + str(case + 1) + ': ' + str(max_v) + ' ' + str(min_v) + '\n')

out = open('C-small-2-attempt1.out', 'w')
for l in result:
    out.writelines(l)
