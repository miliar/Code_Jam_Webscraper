def solve(s, k):
    l = len(s)
    flip_count = 0
    for i in range(l):
        if s[i] == "+":
            continue
        elif s[i] == "-" and l - i < k:
            return "IMPOSSIBLE"
        else:
            s = flip(s, i, k)
            flip_count += 1
    return flip_count


def flip(s, i, k):
    # flip the characters from s[i] to s[i+k-1]
    pre = s[:i]
    concerned = s[i:i + k]
    processed_concerned = []
    post = s[i + k:]
    for index in range(k):
        processed_concerned.append(flip_sign(concerned[index]))
    return pre + "".join(processed_concerned) + post


def flip_sign(ch):
    return "-" if ch == "+" else "+"


if __name__ == "__main__":
    t = int(input())
    for caseno in range(1, t + 1):
        s, kstr = input().strip().split()
        k = int(kstr)
        result = solve(s, k)
        print("Case #{}: {}".format(caseno, result))