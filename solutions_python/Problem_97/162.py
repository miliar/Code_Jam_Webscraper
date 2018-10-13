def solve(A, B):
    count = {}
    visited = [False for i in range(B+1)]
    answer = 0
    for n in range(A, B+1):
        if visited[n]: continue
        s = str(n)
        q = 0
        for i in range(len(s)):
            m = int(s[i:] + s[:i])
            if A <= m <= B:
                if visited[m]: continue
                visited[m] = True
                q += 1
        answer += q * (q-1) / 2
    return answer

if __name__ == '__main__':
    T = int(raw_input())
    for X in range(1, T+1):
        A, B = [int(i) for i in raw_input().split(' ')]
        print "Case #%d: %s" % (X, solve(A, B))
