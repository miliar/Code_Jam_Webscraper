from itertools import combinations

def recycled_pairs(s):
    set_ = set()
    for i in range(len(s)):
        set_.add(int(s[i:] + s[:i]))
    return (tuple(sorted(t)) for t in combinations(set_, 2))

def go(A, B):
    count = 0
    pairs = set()
    for test_num in range(A, B + 1):
        pairs |= set(recycled_pairs(str(test_num)))
    for pair in pairs:
        if A <= pair[0] < pair[1] <= B:
            count += 1
    return count

T = int(raw_input())
for i in range(T):
    line = raw_input()
    A, B = [int(s) for s in line.split()]
    res = go(A, B)
    print 'Case #%i: %i' % (i + 1, res)

# print go(3, 0, [8, 23, 22, 21])