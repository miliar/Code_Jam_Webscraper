def solve(n):
    n = list(n)
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            while i > 0 and n[i] == n[i - 1]:
                i -= 1
            n[i] = chr(ord(n[i]) - 1)
            n = n[:i + 1] + ["9"] * (len(n) - i - 1)
            if i == 0 and n[i] == "0":
                n = n[1:]
            break

    return "".join(n)


def main(inp, out):
    tcn = int(inp.readline())
    for tc in range(tcn):
        n = inp.readline().strip()
        res = solve(n)
        print("Case #{}: {}".format(tc + 1, res), file=out)


if __name__ == "__main__":
    test_name = "B-large"
    main(open(test_name + ".in"), open(test_name + ".out", "w"))
