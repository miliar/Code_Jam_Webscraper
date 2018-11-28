def solve(s):
    ok = True
    for i in range(1, len(s)):
        if s[i] < s[i - 1]:
            ok = False
            break

    if not ok:
        for i in range(len(s) - 1):
            if s[i] >= s[i + 1]:
                s[i] = s[i] - 1
                for j in range(i + 1, len(s)):
                    s[j] = 9
                break

    return int("".join([str(x) for x in s]))


def main():
    t = int(input())
    for i in range(1, t + 1):
        s = [int(x) for x in list(input())]
        print(f"Case #{i}: {solve(s)}")


if __name__ == "__main__": main()