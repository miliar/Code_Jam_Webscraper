import sys

def get_flips_count(str, k):
    arr = [c == '+' for c in str]
    flips = 0
    for i in range(0, len(arr) - k + 1):
        if not arr[i]:
            flips += 1
            for j in range(i, i + k):
                arr[j] = not arr[j]
    if not all(arr[-k:]):
        return -1
    return flips

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open(sys.argv[1])]
    t = int(lines[0])
    for i in range (1, t + 1):
        str, k = lines[i].split(' ')
        res = get_flips_count(str, int(k))
        print('Case #%d: %s' % (i, 'IMPOSSIBLE' if res == -1 else res))
