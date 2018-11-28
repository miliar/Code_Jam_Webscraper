import sys

def read_input(f):
    N = int(f.readline())
    strings = []
    for _ in xrange(N):
        strings += [f.readline().strip()]
    return strings

def count_chars(s):
    if not s:
        return [("", 0)]
    result = []
    current = s[0]
    count = 0
    for i in xrange(len(s)):
        if s[i] == current:
            count += 1
        else:
            result += [(current, count)]
            current = s[i]
            count = 1
    result += [(current, count)]
    return result

def min_moves(strings_w_counts, N):
    moves = 0
    if not all(len(s) == len(strings_w_counts[0]) for s in strings_w_counts):
        return -1
    chars_w_nums = zip(*strings_w_counts)
    for x in chars_w_nums:
        chars = zip(*x)[0]
        if not all(c == chars[0] for c in chars):
            return -1
        lengths = list(zip(*x)[1])
        if min(lengths) != max(lengths):
            moves += min( sum(abs(l - n) for l in lengths)
                          for n in xrange(min(lengths), max(lengths) ) )
    return moves

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for case in xrange(1, T + 1):
        strings = read_input(f)
        strings_w_counts = [ count_chars(s) for s in strings ]
        moves = min_moves(strings_w_counts, len(strings))
        print "Case #%d:" %case,
        if moves < 0:
            print "Fegla Won"
        else:
            print moves
