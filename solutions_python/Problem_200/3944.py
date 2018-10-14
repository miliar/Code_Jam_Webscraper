def read_int():
    return int(raw_input())

def read_str():
    return raw_input()

def solve():
    n = read_str()
    idx = -1
    last = n[0]
    for i in xrange(1,len(n)):
        if n[i] < last:
            idx = i
            break
        last = n[i]
    if idx == -1: return n
    n = list(n)
    for i in xrange(len(n)-1, idx-1, -1):
        n[i] = '9'
    idx -= 1
    n[idx] = str(int(n[idx])-1)
    while idx > 0 and int(n[idx]) < int(n[idx-1]):
        n[idx] = '9'
        n[idx-1] = str(int(n[idx-1])-1)
        idx -= 1
    return str(int(''.join(n)))

def main():
    t = read_int()
    for i in xrange(1,t+1):
        last_tidy = solve()
        print "Case #%d: %s" % (i, last_tidy)

if __name__ == "__main__":
    main()
