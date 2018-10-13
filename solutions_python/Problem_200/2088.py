def solve(nstr):
    l = len(nstr)

    if len(nstr) == 1:
        return nstr

    for i in range(l - 1):
        if nstr[i] <= nstr[i + 1]:
            continue
        else:
            return solve(nstr[:i] + max_smallest(nstr[i:i + 2])) + all_9(
                i + 2, l)

    return nstr


def max_smallest(s):
    # s will be a 2 digit number
    return str(int(s[0]) - 1) + "9"


def all_9(st, ed):
    return "".join(["9" * (ed - st)])


if __name__ == "__main__":
    t = int(input())
    for caseno in range(1, t + 1):
        result = int(solve(input().strip()))
        print("Case #{}: {}".format(caseno, result))