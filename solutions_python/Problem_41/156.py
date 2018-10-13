from sys import stdin

def main():
    T = int(stdin.readline().strip())
    for i in xrange(T):
        n = int(stdin.readline().strip())
        print 'Case #%d: %s' % ((i+1), up(n))


def xperms(str):
    if len(str) <= 1:
        yield str
    else:
        for perm in xperms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]

def up(n):
    s = str(n)
    numbers = []
    while True:
        for perm in xperms(s):
            if int(perm) > n:
                numbers.append(int(perm))
        if len(numbers) > 0:
            break
        else:
            s = s + '0'
    return min(numbers)
    

if __name__ == "__main__":
    main()
