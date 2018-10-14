def main():
    t = int(input())

    for c in range(t):
        s, k = input().split()
        s = list(map(lambda x: True if x == '+' else False, s))
        k = int(k)

        count = 0

        for i in range(len(s) - k + 1):
            if s[i]:
                continue
            else:
                count += 1
                for j in range(k):
                    s[i + j] = not s[i + j]
                i += k

        print(f"Case #{c + 1}: {count if all(s) else 'IMPOSSIBLE'}")


if __name__ == '__main__':
    main()
