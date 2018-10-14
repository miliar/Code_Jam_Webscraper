def min_flips(s, k):
    res = 0
    chars = list(s)
    for i in range(len(s) - k + 1):
        if chars[i] == "-":
            res += 1
            for j in range(k):
                chars[i + j] = "+" if chars[i + j] == "-" else "-"
    if all(ch == "+" for ch in chars):
        return res
    return "IMPOSSIBLE"


def main(inp, out):
    n = int(inp.readline())
    for tc in range(n):
        s, k = inp.readline().split()
        res = min_flips(s, int(k))
        print("Case #{}: {}".format(tc + 1, res), file=out)


if __name__ == "__main__":
    main(open("A-large.in"), open("A-large.out", "w"))
