import sys

values = {}

def value(i, j, k):
    return i + j + k
def is_surprise(i, j, k):
    return j == i+2 or k == i+2 or k == j+2
def is_admisible(i, j, k):
    return i+2 >= k
def max_value(i, j, k):
    return k
def valid(options, p):
    valid = False
    with_surprise = False
    for opt in options:
        if max_value(*opt) >= p:
            if not is_surprise(*opt):
                valid = True
            else:
                with_surprise = True
    return valid, with_surprise

def train():
    global values
    for i in range(11):
        for j in range(11)[i:i+3]:
            for k in range(11)[j:j+3]:
                if not is_admisible(i, j, k):
                    continue
                v = value(i, j, k)
                if v not in values:
                    values[v] = []
                values[v].append((i, j, k))   
                values[v] = list(set(values[v]))

def main():
    with sys.stdin as f:
        for x in range(int(f.readline())):
            solve(f, x+1)

def solve(f, case):
    data = [int(x) for x in f.readline().split(' ')]
    global values
    valids = 0
    surprises = 0
    N = data[0]
    S = data[1]
    p = data[2]
    for i in range(N):
        ti = data[3+i]
        val, sur = valid(values[ti], p)
        if val:
            valids += 1
        elif sur:
            surprises += 1
    total = valids + min(S, surprises)
    print 'Case #%d: %d' % (case, total)

if __name__ == '__main__':
    train()
    main()
