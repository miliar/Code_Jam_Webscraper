import sys

def readline():
    return sys.stdin.readline().rstrip()

def find(n):
    for i in xrange(len(n)-1):
        if n[i] > n[i+1]:
            while i-1 >= 0 and n[i-1] == n[i]:
                i -= 1
            return i
    return -1

def solve(n):
    i = find(n)
    if i != -1:
        n[i] = str(int(n[i])-1)
        for j in xrange(i+1, len(n)):
            n[j] = '9'
    return int(''.join(n))

def main():
    n = int(readline())
    for i in range(1, n+1):
        n = readline()
        print 'Case #%d: %d' % (i, solve(list(n)))

if __name__ == '__main__':
    main()

