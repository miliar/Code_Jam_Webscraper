def flip(s):
    flipped = ''
    for c in s:
        flipped += '+' if c == '-' else '-'

    return flipped


def min_flips(s, K):
    num_flips = 0
    while True:
        start_i = s.find('-')

        if start_i == -1:
            return num_flips

        if start_i > (len(s) - K):
            return 'IMPOSSIBLE'

        s = s[:start_i] + flip(s[start_i : start_i + K]) + s[(start_i + K):]

        num_flips += 1


def main():
    # print min_flips('---+-++-', 3)
    # print min_flips('+++++', 4)
    # print min_flips('-+-+-', 4)

    t = int(raw_input())
    for i in xrange(1, t + 1):
        s, K = raw_input().split(' ')
        print 'Case #%d: %s' % (i, min_flips(s, int(K)))

if __name__ == '__main__':
    main()
