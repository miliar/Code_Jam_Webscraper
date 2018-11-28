import sys

def solve(pancakes, k):
    flip_count = 0
    for i in range(len(pancakes) - k + 1):
        if pancakes[i] == "-":
            flip_count += 1
            for j in range(i, i + k):
                pancakes[j] = {"-": "+", "+": "-"}[pancakes[j]]
    return set(pancakes) == {"+"}, flip_count

def main():
    test_count = int(next(sys.stdin))
    for case_number in range(1, test_count + 1):
        pancakes, k = next(sys.stdin).split()
        pancakes = list(pancakes)
        k = int(k)
        ok, flip_count = solve(pancakes, k)
        if ok:
            print(f"Case #{case_number}: {flip_count}")
        else:
            print(f"Case #{case_number}: IMPOSSIBLE")

if __name__ == "__main__":
    main()
