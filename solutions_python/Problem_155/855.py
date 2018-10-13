'''Standing Ovation problem
For each test case we get the maximum level of shyness s and then
a s+1 digit number containing the number of people who are that shy.

Determine how many people need to be brought so that all people rise to
give a standing ovation'''


def split_s(s, shy):
    e = []
    for i in xrange(s+1):
        e.append(shy % 10)
        shy /= 10
    return e[::-1]


def solve(n):
    s, shy = (int(i) for i in raw_input().split())
    shy = split_s(s, shy)
    summ = shy[0]
    i = 1
    extra = 0
    while i < s+1:
        if i > summ + extra:
            extra = i - summ

        summ += shy[i]
        i += 1
    print "Case #{0}: {1}".format(n + 1, extra)


def main():
    N = int(raw_input())
    for i in xrange(N):
        solve(i)

if __name__ == '__main__':
    main()
