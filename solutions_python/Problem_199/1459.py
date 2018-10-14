import sys


def str2a(s):
    return [c == '+' for c in s]


def a2str(a):
    return ''.join('+' if v else '-' for v in a)


def flip(row, k, idx):
    assert(0 <= idx <= len(row) - k)
    for i in xrange(k):
        row[idx + i] = not row[idx + i]


def get_first_blank(a, k, start=0):
    for i in xrange(start, len(a) - k + 1):
        if not a[i]:
            return i
    return None


def try_fix(a, k):
    count = 0
    is_reversed = False
    if a[0] and not a[-1]:
        a.reverse()
        is_reversed = True
    pos = get_first_blank(a, k)
    while pos is not None and pos <= len(a) - k:
        flip(a, k, pos)
        pos = get_first_blank(a, k, pos + 1)
        count += 1
    if is_reversed:
        a.reverse()
    return count


def fix(s, k):
    a = str2a(s)
    count = try_fix(a, k)
    s_fixed = a2str(a)
    return None if '-' in s_fixed else count


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
      s, k = raw_input().split()
      k = int(k)
      count = fix(s, k)
      print "Case #{}: {}".format(i, count if count is not None else 'IMPOSSIBLE')
      sys.stdout.flush()


if __name__ == "__main__":
    main()

