def solve0(counts, rides):
    counts.insert(0, 0)
    counts2 = [0 for i in range(len(counts))]
    ans = 0
    for i in range(len(counts) - 1, 0, -1):
        if counts[i] + counts2[i] > rides:
            need_sub = orig_ns = counts[i] + counts2[i] - rides
            s = min(need_sub, counts2[i])
            need_sub -= s
            counts2[i] -= s
            s = min(need_sub, counts[i])
            ans += s
            counts[i] -= s
            counts2[i - 1] = orig_ns
    if counts2[0] == 0: return ans

def solve(tickets):
    counts = [0 for i in range(max(x[0] for x in tickets))]
    buyers = [0 for i in range(max(x[1] for x in tickets))]
    for a, b in tickets:
        counts[a - 1] += 1
        buyers[b - 1] += 1
    low = max(buyers) - 1
    high = max(max(counts), low + 1)
    while high - low > 1:
        x = (low + high) // 2
        if solve0(counts[:], x) != None:
            high = x
        else:
            low = x
    return high, solve0(counts[:], high)

for i in range(1, int(input()) + 1):
    print('Case #', i, ': ', ' '.join(map(str, solve(list(tuple(map(int, input().split())) for i in range(int(input().split()[-1])))))), sep='')
