import collections

def main():
    for testcase in range(1, int(input()) + 1):
        print(f"Case #{testcase}: {solve()}")

def split(size):
    return ((size//2) + size%1, ((size-1)//2))

def solve():
    n, k = map(int, input().strip().split())
    d = {n: 1}
    vals = [n]
    vals_ix = 0
    while len(vals) > vals_ix:
        val = vals[0]
        vals = vals[1:]
        count = d[val]
        if count >= k:
            return "{} {}".format(*split(val))
        else:
            k -= count
        for new_val in split(val):
            if new_val not in d:
                vals.append(new_val)
                d[new_val] = 0
            d[new_val] += count

main()
