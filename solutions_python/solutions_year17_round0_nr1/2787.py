FILE = "A0"
FILE = "A-small-attempt0"
FILE = "A-large"


def solve(s, k):
    flipped = 0
    a = list(s)
    for i in range(len(a)):
        if a[i] == "+":
            continue
        if len(a) - i < k:
            return "IMPOSSIBLE"
        for j in range(k):
            a[i + j] = "+" if a[i + j] == "-" else "-"
        flipped += 1
    return flipped


assert solve("---+-++-", 3) == 3, solve("---+-++-", 3)
assert solve("+++++", 4) == 0
assert solve("-+-+-", 4) == "IMPOSSIBLE"

with open(f"{FILE}.in") as f, open(f"{FILE}.out", "w") as w:
    T = int(f.readline())
    for i in range(T):
        S, K = f.readline().split()
        w.write("Case #{}: {}\n".format(
            i + 1, solve(S, int(K))
        ))
