def solve(n, k, s):
    string = [[0 for j in range(k)] for i in range(n)]
    l = len(s)
    stack = []
    for i in range(n):
        for j in range(k):
            string[i][j] = s[i][0][j]
            if string[i][j] != '?':
                stack.append([i, j])
    visited = set()
    while stack:
        i, j = stack.pop()
        if (i, j) in visited: continue
        visited.add((i, j))
        neighs = [(x, y) for x, y in ((i, j + 1), (i, j - 1)) if -1 < x < n and -1 < y < k]
        for (x, y) in neighs:
            if string[x][y] == '?':
                string[x][y] = string[i][j]
                stack.append((x, y))

    check = []
    for i in range(n):
        if string[i][0] == '?':
            check.append(i)

    while check:
        i = check.pop(0)
        if i+1 not in check and i+1 <= n-1:
            for j in range(k):
                string[i][j] = string[i+1][j]
        elif i-1 not in check and i-1 >= 0:
            for j in range(k):
                string[i][j] = string[i-1][j]
        else:
            check.append(i)

    return ''.join(string[i][j] for i in range(n) for j in range(k))





if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        n, k = [int(s) for s in input().split(" ")]
        s = []
        for a in range(n):
            s.append(input().split(" "))
        res = solve(n, k, s)
        print("Case #{}:".format(i))
        start = 0
        end = start + k
        for i in range(n):
            print(res[start:end])
            start = end
            end += k