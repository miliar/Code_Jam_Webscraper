def solve(n,r,y,b):
    if any(map(lambda x: x > n / 2, [y,r,b])):
        return 'IMPOSSIBLE'
    else:
        circle = []
        while min(r,y,b) > 0:
            circle=circle + ['R','Y','B']
            r,y,b=r-1,y-1,b-1
        if not r:
            while min(y,b) > 0:
                circle = circle + ['Y','B']
                y,b=y-1,b-1
        elif not y:
            while min(r,b) > 0:
                circle = circle + ['R','B']
                r,b=r-1,b-1
        else:
            while min(r,y) > 0:
                circle = circle + ['R','Y']
                r,y=r-1,y-1
        if r:
            c = 'R'
            j = r
        elif y:
            c = 'Y'
            j = y
        elif b:
            c = 'B'
            j = b
        else:
            return ''.join(circle)
        i = 0
        while i < len(circle) and j:
            if circle[i] != c != circle[(i+1)%len(circle)]:
                circle = circle[:i+1] + [c] + circle[i+1:]
                j = j - 1
            i = i + 1
    return ''.join(circle)

with open('c:\\python27\\codejam\\outputs.out', 'w') as w, open('c:\\python27\\codejam\\B-small-attempt3.in') as f:
    cases = int(f.readline())
    for case in range(1, cases+1):
        n,r,o,y,g,b,v = map(int,f.readline().split())
        ans = solve(n,r,y,b)
        if ans == "IMPOSSIBLE" or (all(map(lambda x: x not in ans, ['RR','YY','BB'])) and len(ans) == n and (ans.count('R') == r and ans.count('Y') == y and ans.count('B') == b and ans[0] != ans[-1])):     
            w.write('Case #{0}: {1}\n'.format(case, ans))
        else:
            w.write('Case #{0}: {1}\n'.format(case, 'SOMETHING OFF'))
        
