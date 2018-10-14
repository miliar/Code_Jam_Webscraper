

def solve(s, k):
    s = [ch for ch in s]
    ans = 0
    for i in range(len(s)-k+1):
        if s[i] == '-':
            for j in range(k):
                s[i+j] = '-' if s[i+j] == '+' else '+'
            ans += 1
    for ch in s[-k+1:]:
        if ch == '-':
            return "IMPOSSIBLE"
    return str(ans)

with file("2.txt", "r") as in_file:
    with file("ans.txt", "w") as out_file:
        i = 0
        for row in in_file:
            d = row.split()
            if len(d) < 2:
                continue
            i += 1
            print >>out_file, "Case #%d:"%i, solve(d[0], int(d[1]))