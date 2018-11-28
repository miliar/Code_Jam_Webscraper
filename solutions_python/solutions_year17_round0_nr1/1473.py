def solution(S, K):
    flips = [0 for x in xrange(0, K)]
    total_flips = 0
    # Special cases!
    for start_position in xrange(0, len(S) - K + 1):
        if (S[start_position] == '-' and flips[0] % 2 == 0)\
                or (S[start_position] == '+' and flips[0] % 2 != 0):
            total_flips += 1
            for index in xrange(0, K):
                flips[index] += 1
        flips = flips[1:]
        flips.append(0)
    # if S[len(S) - K + 1 :].count('-') > 0:
    for pancake, flip in zip(S[len(S) - K + 1 :], flips):
        if (pancake == '-' and flip % 2 == 0) \
                or (pancake == '+' and flip % 2 != 0):
            return 'IMPOSSIBLE'
    return total_flips

files = [
    'A-large.in'
]

if __name__ == '__main__':
    for filename in files:
        outfilename = filename.replace('.in', '.out')
        with open(filename, 'r') as f:
            with open(outfilename, 'w') as w:
                no_lines = int(f.readline())
                results = []
                for index in xrange(0, no_lines):
                    S, K = f.readline().strip('\n').split()
                    print 'Processing case {}'.format(index + 1)
                    result = solution(S, int(K))
                    w.writelines("Case #{}: {}\n".format(index +1, result))
