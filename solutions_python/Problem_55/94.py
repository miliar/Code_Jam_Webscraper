
def ThemePark():
    R, k, N = map(int, raw_input().split())
    G = map(int, raw_input().split())
    C = [None] * N
    result = 0
    i = 0
    while R > 0:
        if C[i]:
            R0, result0 = C[i]
            dR = R0 - R
            cycles = R / dR
            if cycles:
                R -= cycles * dR
                result += cycles * (result-result0)
                continue
        else:
            C[i] = R, result
        count = 0
        j = i
        while count+G[j] <= k:
            count += G[j]
            j = (j+1) % N
            if j == i:
                break
        i = j
        R -= 1
        result += count
    print result

#---------------------------------------------------------------

T = int(raw_input())
for testcase in range(T):
    print "Case #%d:" % (testcase+1),
    ThemePark()
