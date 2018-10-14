
def solve(data):
    sMax, s = data
    answer = 0
    sum = 0
    for i in xrange(1, sMax + 1):
        sum += s[i - 1]
        if sum < i:
            answer += i - sum
            sum = i
    return answer

def get_input():
    sMax, s = raw_input().split()
    return int(sMax), [int(s[i]) for i in xrange(int(sMax) + 1)]

def main():
    T = int(raw_input())
    for i in xrange(T):
        print 'Case #%d: %s' % (i + 1, solve(get_input()))

if __name__ == '__main__':
    main()
