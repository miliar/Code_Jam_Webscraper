input_file = 'tests.txt'

def recycled(n, m):
    n = str(n)
    m = str(m)
    for i in xrange(len(n)):
        if n[i:] + n[:i] == m:
            return True
    return False

def solve(A, B):
    result = 0
    for n in xrange(A, B + 1):
        for m in xrange(n + 1, B + 1):
            if recycled(n, m):
                result += 1
    return result

def main():
    fh = open(input_file)
    test_cases = int(fh.readline())
    for case in xrange(test_cases):
        A, B = [int(x) for x in fh.readline().split()]
        print 'Case #%s: %s' % (case + 1, solve(A, B))
    
    
if __name__ == '__main__':
    main()
