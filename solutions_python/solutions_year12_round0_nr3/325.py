def solve(A, B):
    count = 0
    for n in range(A, B):
        seen = set()
        digits = str(n)
        k = len(digits)
        for i in range(1, k):
            if digits[i] != 0:
                m = int(digits[i:] + digits[:i])
                if n < m <= B and m not in seen:
                    count += 1
                    seen.add(m)
    return count

T = int(input())
for i in range(1, T + 1):
    A, B = map(int, input().split())
    print("Case #%d: %s" % (i, solve(A, B)))
