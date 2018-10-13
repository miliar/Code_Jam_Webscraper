def can_do_one(duration, count, vals):
    while duration > 0:
        vals.sort()
        if vals[-1] > duration - count:
            vals[-1] = vals[-1] - (duration - count)
            vals.append(duration - count)
            count -= 1
        else:
            vals = [v - 1 for v in vals]
        duration -= 1
    return count == 0 and max(vals) <= 0

def can_do(duration, vals):
    for count in range(max(vals) + 1):
        if can_do_one(duration, count, vals[:]):
            return True
    return False

def solve(test_case):
    raw_input()
    vals = [int(s) for s in raw_input().split()]
    lo = 0
    hi = max(vals)
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if can_do(mid, vals[:]):
            hi = mid
        else:
            lo = mid
    print("Case #%d: %d" % (test_case, hi))

if __name__ == "__main__":
    test_cases = int(raw_input())
    for test_case in range(test_cases):
        solve(test_case + 1)
