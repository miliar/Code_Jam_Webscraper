def read_string():
    test_str = input()
    test_str, tmp = test_str.split(" ")
    f_len = int(tmp)
    return list(test_str), f_len


def process(s, f_len):
    def flip(idx):
        if len(s) - idx + 1 > f_len:
            for i in range(idx, idx + f_len):
                s[i] = "+" if s[i] == "-" else "-"
            return True
        else:
            return False

    if f_len == 1:
        return str(len(s))
    flip_cnt = 0
    i = 0
    while i < len(s):
        if s[i] == "-":
            if not flip(i):
                return "IMPOSSIBLE"
            else:
                flip_cnt = flip_cnt + 1
        i = i + 1

    return str(flip_cnt)


test_cnt = int(input())

for t_idx in range(1, test_cnt + 1):
    s, f_len = read_string()
    print("Case #" + str(t_idx) + ": " + process(s, f_len))