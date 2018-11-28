def next_valid_line(p, j):
    for i in range(j, len(p)):
        if p[i][0] != '?':
            return p[i]
    return None

def prev_valid_line(p, j):
    for i in reversed(range(0, j)):
        if p[i][0] != '?':
            return p[i]

def solve(p):
    # Keep going down until you hist something
    n = [] 
    c = ''
    i = 0
    j = 0
    found = False

    for i in range(0, len(p)):
        found = False
        c = ''
        j = 0

        while j < len(p[0]): 
            if found is False: 
                if p[i][j] != '?': 
                    c = p[i][j] 
                    found = True
                    j = -1
            else:
                if p[i][j] == '?':
                    p[i][j] = c
                else:
                    c = p[i][j] 
            j += 1
    
    # Handle empty rows 
    for i in range(0, len(p)): 
        if p[i][0] == '?':
            n = next_valid_line(p, i)  
            p[i] = n if n is not None else prev_valid_line(p, i)

    # Run again to handle empty first rows
    if p[-1][0] == '?':
        p[-1] = p[-2]

    return p

t = int(input())
for i in range(0, t):
    inpc = list(map(int, input().strip().split(' ')))
    inp = [ list(input().strip()) for j in  range(0, inpc[0]) ]
    inp = solve(inp)

    s = 'Case #{}:\n'.format(i+1)
    for l in inp:
        s += ''.join(l) + '\n'
    print(s[:-1])

