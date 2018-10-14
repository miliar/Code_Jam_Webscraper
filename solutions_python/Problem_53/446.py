# Google Code Jam 2010.
# Larry Engholm, 5/7/2010

# Problem description:
# http://code.google.com/codejam/contest/dashboard?c=433101

def test(n, k):
    while n > 0:
        if k % 2 == 0:
            return False
        k = k >> 1
        n = n - 1
    return True

def main():
    file = open('c:/Documents and Settings/Larry/My Documents/Downloads/A-large.in')
    numLines = int(file.readline())
    for i in range(numLines):
        (n, k) = map(int, file.readline().split())
        print 'Case #{0}: {1}'.format(i+1, ("OFF","ON")[test(n,k)])
main()
