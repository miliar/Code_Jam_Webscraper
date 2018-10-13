def solve(a, b, k):
    cnt = 0
    for i in xrange(a):
        for j in xrange(b):
            if i & j < k:
                cnt += 1
    return cnt

def main():
    n = int(raw_input().strip())
    for y in xrange(n):
        case = [int(x.strip()) for x in raw_input().split()]
        print "Case #%d: %d" % (y + 1, solve(case[0], case[1], case[2]))

if __name__ == '__main__':
    main()
