def main():
    for testcase in range(1, int(input()) + 1):
        print(f"Case #{testcase}: {solve()}")

def solve():
    pancakes, k = input().split()
    k = int(k)
    pancakes = list(pancakes)
    count = 0

    for i in range(len(pancakes) - k + 1):
        if pancakes[i] == '-':
            count += 1
            for j in range(i, i + k):
                pancakes[j] = '-' if pancakes[j] == '+' else '+'

    solved = pancakes == ['+'] * len(pancakes)
    return count if solved else "IMPOSSIBLE"


main()
