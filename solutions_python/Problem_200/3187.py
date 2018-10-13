def main():
    t = int(input())

    for c in range(t):
        n = int(input())
        while not tidy(n):
            n -= 1
        print(f"Case #{c + 1}: {n}")


def tidy(n):
    digits = list(map(int, str(n)))
    return all([digits[i] <= digits[i + 1] for i in range(len(digits) - 1)])


if __name__ == '__main__':
    main()
