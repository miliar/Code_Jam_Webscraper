T = int(raw_input())
for i in range(1, T+1):
    a, b = raw_input().split()
    a, b = int(a), int(b)
    solution = 0
    if b > 20:
        for n in range(a, b):
            n_str = str(n)
            for m in range(n+1, b+1):
                m_str = str(m)
                if len(n_str) != len(m_str):
                    break
                for j in range(1, len(n_str)):
                    tmp = n_str[:j]
                    new_n = n_str[j:] + tmp
                    if new_n == m_str:
                        solution += 1
                        break
    print "Case #%d: %d" % (i, solution)