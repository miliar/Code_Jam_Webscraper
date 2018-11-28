import sys
def large(n, left, right):
    if not isinstance(n, list):
        n = list(n)
    for i in xrange(left, right):
        p, q = int(n[i-1]), int(n[i])
        if q<p:
            n[i - 1] = str(p-1)
            for j in xrange(i, len(n)):
                n[j] = '9'
            large(n, 1, i+1)
    return ''.join(n)
def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        # T = int(lines[0].strip())
        for i in xrange(1, len(lines)):
            n = lines[i].strip()
            ans = large(n, 1, len(n))
            if ans[0] == '0':
                print 'Case #{}: {}'.format(i, ans[1:])
            else:
                print 'Case #{}: {}'.format(i, ans)
            

if __name__ == "__main__":
    main()