def solve_line(l):
    t = solve_line_first(l)
    return solve_line_first(t[::-1])[::-1]

def solve_line_first(l):
    prev = '?'
    s = ''
    for c in l:
        if c == '?':
            s += prev
        else:
            s += c
            prev = c
    return s

def solve_first(lines, c):
    res = []
    q = '?' * c
    prev = '?' * c
    for line in lines:
        if line == q:
            res.append(prev)
        else:
            prev = solve_line(line)
            res.append(prev)
    return res

def solve(lines, c):
    res = solve_first(lines, c)
    return '\n'.join(solve_first(res[::-1], c)[::-1])

for i in range(int(input())):
    r, c = input().split()
    lines = [input() for _ in range(int(r))]
    print('Case #{}: \n{}'.format(i+1, solve(lines, int(c))))
