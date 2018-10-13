def solve(r, c, s):
    prevString = ''
    result = []
    prevRow = -1
    for i in range(r):
        row = ''
        nowCha = ''
        now = -1
        for j in range(c):
            if s[i][j] != '?':
                row += s[i][j]* (j - now)
                now = j
                nowCha = s[i][j]
        if row:
            row += nowCha  * (c-now-1)
            for j in range(prevRow+1, i+1):
                result.append(row)
            prevString = row
            prevRow = i
    for i in range(prevRow+1, r):
        result.append(prevString)
    return result

T = int(input())
for i in range(1, T+1):
    R, C = [int(x) for x in input().split(' ')]
    s = []
    for j in range(R):
        s.append(input())
    print('Case #{}:'.format(i))
    result = solve(R, C, s)
    for j in range(R):
        print (result[j])
