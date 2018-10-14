import sys

memo = {}
def solve(s, k, memo, visited, top=False):
    assert all(c in ('+', '-') for c in s)
    if s in memo:
        return memo[s]
    if s in visited:
        return None
    visited[s] = True
    if all(c == '+' for c in s):
        memo[s] = 0
        return 0
    min_val = 10 ** 20
    for start_split in range(len(s) - k + 1):
        left = s[:start_split]
        old_middle = s[start_split:start_split + k]
        assert(len(old_middle) == k)
        middle = ''.join('+' if c == '-' else '-' for c in old_middle)
        assert(len(middle) == k)
        right = s[start_split + k:]
        for right_split in range(k):
            middle_left = middle[:right_split]
            middle_right = middle[right_split:]
            full_left = left + middle_left
            full_right = middle_right + right
            left_amount = solve(full_left, k, memo, visited)
            right_amount = solve(full_right, k, memo, visited)
            if left_amount is not None and right_amount is not None:
                if top:
                    pass
                    #print start_split
                    #print left
                    #print middle
                    #print right
                    #print ('{}|{} -> {}|{}'.format(full_left, full_right, left_amount, right_amount))
                this_val = 1 + left_amount + right_amount
                min_val = min(this_val, min_val)
    if min_val == 10 ** 20:
        min_val = None
    memo[s] = min_val
    return min_val


t = int(next(sys.stdin))
for test in range(t):
    s, k_str = next(sys.stdin).strip().split(' ')
    k = int(k_str)
    retval = solve(s, k, {}, {}, True)
    if retval is None:
        retval = 'IMPOSSIBLE'
    print ('Case #{}: {}'.format(test+1, retval))
