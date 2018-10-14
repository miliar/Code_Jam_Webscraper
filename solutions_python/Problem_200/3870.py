import sys

def tidy_numbers(N):
    s = [int(c) for c in str(N)]
    #print(s)

    # First we find the first non-tidy digit pair
    bad_index = -1
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            bad_index = i
            break

    if bad_index < 0:
        return N

    while bad_index > 0 and s[bad_index] == s[bad_index - 1]:
        bad_index -= 1

    if s[bad_index] == 1:
        return int('9' * (len(s) - 1))

    return int(''.join([str(c) for c in s[0:bad_index] + [s[bad_index] - 1] + ['9'] * len(s[bad_index+1:])]))


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        T = int(f.readline())
        for i in range(T):
            N = int(f.readline())
            print("Case #%d: %s" % (i + 1, tidy_numbers(N)))
