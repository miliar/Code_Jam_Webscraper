in_file_name = './A-large.in'

def solve(s, k):
    n = len(s)
    a = list(s)
    i = 0
    res = 0
    while i < n:
        if a[i] == '-':
# do flip
            j = i
            if j + k - 1 >= n:
                return -1

            while j < i + k:
                if a[j] == '-':
                    a[j] = '+'
                else:
                    a[j] = '-'
                j += 1
            res += 1
        i += 1
    return res

with open(in_file_name, 'r') as f:
        lines = f.readlines()
        T = int(lines[0])
        for tn in range(1, T + 1):
            w1, w2 = lines[tn].split()
            S = w1
            K = int(w2)
            res = solve(S, K)
            v = str(res)
            if res == -1:
                v = 'IMPOSSIBLE'
            print 'Case #%d: %s' % (tn, v)

