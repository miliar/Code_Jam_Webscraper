def simulate(k, state):
    e = 0
    i = 0
    while i < len(state):
        if e + state[i] <= k:
            e += state[i]
        else:
            break
        i += 1
    return e, state[i:] + state[:i]

def ans(r, k, state):
    seen = {state: (0, 0)}
    i = 1
    m_sum = 0
    m_sums = []
    while True:
        m, state = simulate(k, state)
        if state in seen:
            break
        m_sums.append(m_sum)
        m_sum += m
        seen[state] = (m_sum, i)
        i += 1
        if i == r + 1:
            return m_sum

    m_sums.append(m_sum)

    loop_money = m_sum - seen[state][0] + m
    loop_size = i - seen[state][1]

    non_loop_money = seen[state][0]
    non_loop_size  = seen[state][1]

    m_sums = [x - non_loop_money for x in m_sums[non_loop_size:]]

    R = r - non_loop_size
    d = R / loop_size
    m = R % loop_size

    return non_loop_money + d * loop_money + m_sums[m]    

T = int(raw_input())
for t in range(1, T+1):
    R, k, N = map(int, raw_input().split())
    state = tuple(map(int, raw_input().split()))
    print 'Case #%d: %d' % (t, ans(R, k, state))
