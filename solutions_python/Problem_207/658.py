def main():
    t = int(input().strip())
    for case in range(1, t + 1):
        n, r, ry, y, yb, b, br = map(int, input().split())
        colors = {}
        colors['R'] = r
        colors['O'] = ry
        colors['Y'] = y
        colors['G'] = yb
        colors['B'] = b
        colors['V'] = br

        sol = construct_solution(n, colors)
        print('Case #{}: {}'.format(case, sol))

def construct_solution(n, cols):
    imp = 'IMPOSSIBLE'
    bases = ['R', 'Y', 'B']
    comps = ['G', 'V', 'O']
    ns = {'G': 'R', 'V': 'Y', 'O': 'B',
          'R': 'G', 'Y': 'V', 'B': 'O'}

    if sum(cols[b] for b in bases) == 0:
        return imp
    start = next(c for c in bases if cols[c] > 0)
    s = start
    cols[start] -= 1
    cur = start
    while len(s) < n:
        if cur in comps:
            nx = ns[cur]
            if cols[nx] == 0:
                return imp
        else:
            if cols[ns[cur]] != 0:
                nx = ns[cur]
            else:
                cands = [b for b in bases if b != cur and cols[b] != 0]
                if len(cands) == 0:
                    return imp
                nx = cands[0]
                if len(cands) > 1:
                    if cols[nx] < cols[cands[1]]:
                        nx = cands[1]
        cur = nx
        s += cur
        cols[cur] -= 1
    first = s[0]
    if are_compatible(first, cur):
        return s
    else:
        return imp

def are_compatible(a, b):
    ns = {'R' : {'Y', 'B', 'G'},
          'B' : {'Y', 'R', 'O'},
          'Y' : {'R', 'B', 'V'},
          'O' : {'B'},
          'G' : {'R'},
          'V' : {'Y'},}
    if b in ns[a]:
        return True
    else:
        return False

#def is_impossible(n, r, ry, y, yb, b, br):
#    pairs = [(ry, b), (yb, r), (br, y)]
#    if any(x > y for x, y in pairs):
#        return True
#    if any(x != 0 and x == y for x, y in pairs):
#        if max(map(sum, pairs)) == n:
#            return False
#        else:
#            return True
#    b -= ry
#    r -= yb
#    y -= br
#    bases = [b, r, y]
#    if max(bases) > sum(bases) // 2 or \
#       (b + r) % 2 == 1 or\
#       (y + r) % 2 == 1 or\
#       (y + b) % 2 == 1:
#        return True
#    else:
#        return False





if __name__ == '__main__':
    main()
