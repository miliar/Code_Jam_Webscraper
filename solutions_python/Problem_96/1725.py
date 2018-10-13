import sys

def parse(line):
    l = map(lambda x: int(x), line.split(' '))
    (n, s, p) = l[0:3]
    t = l[3:]
    return (n, s, p, t)
    
def solve(line):
    (n, s, p, t) = parse(line)
    if p == 0:
        return n
    a = len(filter(lambda x: x > 3 * p - 3, t))
    b = min(len(filter(lambda x: x > 1 and x in (3 * p - 3, 3 * p - 4), t)), s)
    return a + b

def main():
    T = int(sys.stdin.readline())
    i = 0
    for i in range(1, T+1):
        line = sys.stdin.readline()
        if line == '':
            break
        sys.stdout.write("Case #%d: %d\n" % (i, solve(line)))

def test():
    print solve('3 0 8 23 22 21')

if __name__ == "__main__":
    main()
