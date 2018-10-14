# tidy.py
def test(n): # cake, flipper

    x, s, c = n, str(n), 0
    for i in range(len(s) - 1):
        if s[i+1] > s[i]: c = i + 1
        if s[i+1] < s[i]:
            x = str(int(s[:c + 1]) - 1) + "9" * (len(s) - c - 1)
            break
    return int(x)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())
    print("Case #{}: {}".format(i, test(n)))
