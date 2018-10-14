def answer(pancakes_str, k):
    result = 0
    pancakes_count = len(pancakes_str)
    pancakes = [0 if pancake == '-' else 1 for pancake in pancakes_str]

    for i in range(pancakes_count - k + 1):
        if pancakes[i] == 0:
            result += 1
            for j in range(i, i + k):
                pancakes[j] = 1 - pancakes[j]

    for i in range(pancakes_count - k + 1, pancakes_count):
        if pancakes[i] == 0:
            result = -1

    return result


def main():
    t = int(input())
    for i in range(1, t + 1):
        pancakes_str, k_str = input().split(" ")
        result = answer(pancakes_str, int(k_str))
        if result == -1:
            result = "IMPOSSIBLE"
        print("Case #{}: {}".format(i, result))


if __name__ == "__main__":
    main()
