def flip(n):
    n = ['-' if e == '+' else '+' for e in n]
    return n

def do_work(n, k):
    flips = 0
    minus = 0
    try:
        minus = n.index('-')
    except ValueError:
        return 0
    last_minus = -1
    while last_minus <= minus:
        if minus + k > len(n):
            return 'IMPOSSIBLE'
        last_minus = minus
        first = n[:minus]
        chunk = n[minus: minus + k]
        rest = n[minus+k:]
        chunk = flip(chunk)
        flips += 1
        n = first+chunk+rest
        try:
            minus = n.index('-')
        except ValueError:
            break
    try:
        minus = n.index('-')
        return "IMPOSSIBLE"
    except ValueError:
        return flips




t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = input().split()
    n, k = list(n), int(k)
    n2 = n[::-1]
    result = do_work(n, k)
    result2 = do_work(n, k)
    print("Case #{}: {}".format(i, result))
