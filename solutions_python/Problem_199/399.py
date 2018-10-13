def zero(bits, i):
    while True:
        if 1 << i & bits == 0:
            return i
        i += 1

def solve(bits, n, k):
    allone = int('1' * n, 2)
    mask = int('1' * k, 2)
    d = 0
    i = 0
    while True:
        z = zero(bits, i)
        if z <= n - k:
            bits ^= mask << z
            i = z
        elif z == n:
            return d
        else:
            return "IMPOSSIBLE"
        d += 1

t = int(input())
for i in range(1, t + 1):
  s, k = input().split(" ")
  print("Case #{}: {}".format(i, solve(int(''.join('1' if c == '+' else '0' for c in s), 2), len(s), int(k))))
