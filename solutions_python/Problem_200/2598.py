def isTidy(s):
    prev = s[0]
    for d in s[1:]:
        if d < prev:
            return False
        prev = d
    return True

for t in range(int(input())):
    N = int(input())
    mask = 10
    while not isTidy(str(N)):
        N -= N%mask
        N -= 1
        mask *= 10

    print("Case #{}: {}".format(t + 1, N))
