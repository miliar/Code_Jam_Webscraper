import sys

sys.setrecursionlimit(1500)


def inv(so_far, i, cnt):
    if cnt[i] == 0:
        return inv(so_far, i + 1, cnt)
    r = 0 if so_far >= i else i - so_far
    if i + 1 < len(cnt):
        return r + inv(so_far + cnt[i] + r, i + 1, cnt)
    return r

in_file = open(sys.argv[1])
num_cases = int(in_file.readline().rstrip('\n'))

for n in range(num_cases):
    line = in_file.readline().rstrip('\n').split(' ')
    max_shy = int(line[0])
    shy_count = map(lambda x: int(x), list(line[1]))
    assert max_shy + 1 == len(shy_count)
    print 'Case #%i: %i' % (n + 1, inv(0, 0, shy_count))
