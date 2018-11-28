FILE = "B0"
FILE = "B-small-attempt0"
FILE = "B-large"

def solve(s):
    for i in range(1, len(s)):
        if s[0] < s[i]:
            return s[:i] + solve(s[i:])

        if s[0] > s[i]:
            return str(int(s[0]) - 1) + "9" * (len(s) - 1)

    return s


with open(f"{FILE}.in") as f, open(f"{FILE}.out", "w") as w:
    T = int(f.readline())
    for i in range(T):
        N = f.readline().strip()
        w.write("Case #{}: {}\n".format(
            i + 1, int(solve(N))
        ))
