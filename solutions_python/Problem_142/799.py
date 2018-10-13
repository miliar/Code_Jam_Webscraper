__author__ = 'Alen'

import sys

# sys.stdin = open('A.in')

N = int(sys.stdin.readline().strip())
for qw in range(1, N+1):
    print 'Case #%d:' % qw,

    N = int(sys.stdin.readline().strip())
    strs = []
    for i in range(N):
        s = sys.stdin.readline().strip()
        strs.append(s)

    c_all_counts = []
    c_count_counts = []
    previous_m_str = ''
    ctn = False
    for s in strs:
        m_str = ''
        previous_c = s[0]
        m_str += previous_c
        c_counts = [1,]
        for c in s[1:]:
            if c == previous_c:
                c_counts[-1] += 1
            else:
                previous_c = c
                m_str += previous_c
                c_counts.append(1)
        if previous_m_str and previous_m_str != m_str:
            print('Fegla Won')
            ctn = True
            break
        else:
            previous_m_str = m_str
            if c_count_counts:
                for i in range(len(c_count_counts)):
                    c_count_counts[i] += c_counts[i]
            else:
                c_count_counts = c_counts[:]
            c_all_counts.append(c_counts)

    if ctn:
        continue

    c_avg_counts = [x / N for x in c_count_counts]

    moves2 = []
    for i in range(N):
        moves = []
        for j in range(len(c_avg_counts)):
            moves.append(abs(c_avg_counts[j] - c_all_counts[i][j]))
        moves2.append(sum(moves))
    print(sum(moves2))