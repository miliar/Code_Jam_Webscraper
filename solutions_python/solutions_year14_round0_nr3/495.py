import sys

t = int(sys.stdin.readline())

def gen(r, c, m):
    if r < c:
        pos, ans = gen(c, r, m)
        if pos:
            return pos, [[l[i] for l in ans] for i in range(len(ans[0]))]
        else:
            return False, [[]]
    elif m == 0:
        ans = [["." for i in range(c)] for i in range(r)]
        ans[0][0] = 'c'
        return True, ans
    elif m == r * c - 1:
        ans = [["*" for i in range(c)] for i in range(r)]
        ans[0][0] = 'c'
        return True, ans
    else:
        if c == 1:
            return True, [['c']] + [['.'] for i in range(r - m - 1)] + [['*'] for i in range(m)]
        elif c == 2:
            if r == 2:
                return False, [[]]
            else:
                pos, ans = gen(r - 1, c, m - 2)
                if pos:
                    return True, ans + ['*' * c]
                else:
                    return False, [[]]
        elif c == 3:
            pos, ans = gen(r - 1, c, m - 3)
            if pos:
                return True, ans + ['*' * c]
            else:
                pos ,ans = gen(r - 1, c , m - 1)
                if pos and ans[-1][1] != '*':
                    return True, ans + ['.' * 2 + '*']
                else:
                    return False, [[]]
        elif c == 4:
            pos, ans = gen(r - 1, c, m - 4)
            if pos:
                return True, ans + ['*' * c]
            else:
                pos, ans = gen(r - 1, c , m - 2)
                if pos and ans[-1][1] != '*':
                    return True, ans + ['.' * 2 + '*' * 2]
                else:
                    pos, ans = gen(r - 1, c, m - 1)
                    if pos and ans[-1][2] != '*':
                        return True, ans + ['.' * 3 + '*']
                    else:
                        return False, [[]]
        elif c == 5:
            pos, ans = gen(r - 1, c, m - 5)
            if pos:
                return True, ans + ['*' * c]
            else:
                pos, ans = gen(r - 1, c , m - 3)
                if pos and ans[-1][1] != '*':
                    return True, ans + ['.' * 2 + '*' * 3]
                else:
                    pos, ans = gen(r - 1, c, m - 2)
                    if pos and ans[-1][2] != '*':
                        return True, ans + ['.' * 3 + '*' * 2]
                    else:
                        pos, ans = gen(r - 1, c, m - 1)
                        if pos and ans[-1][3] != '*':
                            return True, ans + ['.' * 4 + '*']
                        else:
                            return False, [[]]
                        
    return False, [[]]
    
for i in range(t):
    sys.stdout.write("Case #{0}:\n".format(str(i + 1)))
    r, c, m = map(int, sys.stdin.readline().split())
    pos, ans = gen(r, c, m)
    if pos:
        for l in ans:
            for p in l:
                sys.stdout.write(p)
            sys.stdout.write("\n")
    else:
        sys.stdout.write("Impossible\n")