
def solve():
    N = int(raw_input())
    matrix = [raw_input().rfind('1') for i in xrange(N)]

    count = 0
    for i in xrange(N-1):
        if matrix[i] - i > 0:
            pos = i
            for j in xrange(i + 1, N):
                if matrix[j] <= i :
                    pos = j
                    break
            for j in xrange(pos, i, -1):
                matrix[j], matrix[j-1] = matrix[j-1], matrix[j]
                count += 1
    return count

def main():
    T = int(raw_input())
    for i in xrange(T):
        print 'Case #%d: %s' % (i + 1, solve())

if __name__ == '__main__':
    main()

