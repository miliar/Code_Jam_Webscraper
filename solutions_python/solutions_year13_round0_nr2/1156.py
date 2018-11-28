lines = [line.strip() for line in open('large_input.txt').readlines() if line.strip()]
num_cases = int(lines[0])

def ext_vals(lawn):
    temp = sorted(list(set([i for j in lawn for i in j])))
    return (temp[0], temp[-1])

def secmin_val(lawn):
    return sorted(list(set([i for j in lawn for i in j])))[1]

def iter_(lawn):
    minval, maxval = ext_vals(lawn)
    if minval == maxval:
        return 'YES'

    secminval = secmin_val(lawn)
    new_lawn = [[c for c in row] for row in lawn]
    n, m = len(lawn), len(lawn[0])
    found = False
    for row in range(n):
        if all([lawn[row][i]==minval for i in range(m)]):
            found = True
            for i in range(m):
                new_lawn[row][i] = secminval
    for col in range(m):
        if all([lawn[i][col]==minval for i in range(n)]):
            found = True
            for i in range(n):
                new_lawn[i][col] = secminval
    if found:
        return iter_(new_lawn)
    return 'NO'

i = 1
case = 1
while i < len(lines):
    n, m = [int(k) for k in lines[i].split()]
    i += 1
    lawn = []
    for j in range(n):
        row = [int(k) for k in lines[i].split()]
        lawn.append(row)
        i += 1
    print 'Case #%i: %s' % (case, iter_(lawn))
    case += 1
