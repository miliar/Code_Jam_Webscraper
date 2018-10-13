def other_char(char):
    tmp = {"R", "B", "Y"}
    tmp.remove(char)
    return tmp


def can_i_use(r, y, b, char, last_char):
    cnt = {"R": r, "B": b, "Y": y}
    if char == last_char or cnt[char] <= 0:
        return False
    oth_ch = other_char(char)
    for ch in oth_ch:
        if cnt[ch] > cnt[char] and ch != last_char:
            return False
    return True


def is_valid(output, r, y, b):
    ccnt = {"R": r, "Y": y, "B": b}
    for i in range(1, len(output)):
        if output[i] == output[i - 1]:
            return False
    if output[-1] == output[0] and len(output) > 1:
        return False
    for ch in output:
        ccnt[ch] -= 1
    assert ccnt["R"] == 0 and ccnt["Y"] == 0 and ccnt["B"] == 0
    return True


def solve(r, y, b):
    ir, iy, ib = r, y, b
    if 2 * max(r, y, b) > (r + y + b):
        return "IMPOSSIBLE"
    output = ""
    while (r + y + b) > 0:
        last_chr = "" if output == "" else output[-1]

        if r > 0 and (output == "" or can_i_use(r, y, b, "R", last_chr)):
            output += "R"
            r -= 1
        elif y > 0 and (output == "" or can_i_use(r, y, b, "Y", last_chr)):
            output += "Y"
            y -= 1
        elif b > 0 and (output == "" or can_i_use(r, y, b, "B", last_chr)):
            output += "B"
            b -= 1
        else:
            assert False
    assert is_valid(output, ir, iy, ib)
    return output


def main():
    t_case = int(input())
    for i in range(t_case):
        _, r, _, y, _, b, _ = map(int, input().split())
        print("Case #{}: {}".format(i + 1, solve(r, y, b)))


if __name__ == "__main__":
    import sys

    sys.stdin = open("B-small-attempt2.in", "r")
    sys.stdout = open("out", "w")
    main()
