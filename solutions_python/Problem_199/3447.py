def read_str():
    return raw_input()

def read_int():
    return int(raw_input())

def solve_recursive(current, n, visited, size):
    new_l = list()
    for s in current[n]:
        if s == ['+'] * len(s): return n
        for i in xrange(len(s)-(size-1)):
            new_s = list(s)
            for j in xrange(size):
                new_s[i+j] = '-' if new_s[i+j] == '+' else '+'
            if new_s not in visited:
                new_l.append(new_s)
                visited.append(new_s)
    if len(new_l) == 0:
        return -1
    current[n+1] = list(new_l)
    return solve_recursive(current, n+1, visited, size)
    

def solve():
    t_c = read_str().strip().split(" ")
    size = int(t_c[1])
    s = t_c[0]
    s = list(s)
    current = dict()
    current[0] = [s]
    n = solve_recursive(current, 0, list(), size)
    if n == -1: return "IMPOSSIBLE"
    return str(n)

def main():
    t = read_int()
    for i in xrange(1,t+1):
        n = solve()
        print "Case #%d: %s" % (i, n)

if __name__ == "__main__":
    main()
