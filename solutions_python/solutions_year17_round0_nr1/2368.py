def solve(s, k):
    result = 0

    for i in range(0, len(s) - k + 1):
        if s[i] == '+':
            continue

        for j in range(i, i + k):
            s[j] = '+' if s[j] == '-' else '-'
        result += 1

    for x in s:
        if x == '-':
            return "IMPOSSIBLE"

    return result


def main():
    t = int(input())
    for i in range(1, t + 1):
        s, k = input().split(" ")
        k = int(k)

        print(f"Case #{i}: {solve(list(s), k)}")


if __name__ == "__main__": main()
