def is_sorted(a):
    w = a[:]
    w.sort()
    if w == a:
        return True
    else:
        return False

def solve(n):
    for i in range(n, -1, -1):
        if is_sorted(list(str(i))):
            return i

if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        last = solve(n)
        print("Case #{}: {}".format(i, last))
