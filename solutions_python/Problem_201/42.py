from collections import defaultdict

t = int(input())

def do_task():
    n, k = map(int, input().split())
    spaces = defaultdict(int)
    spaces[n] = 1
    while True:
        newspaces = defaultdict(int)
        for size, count in sorted(spaces.items(), reverse=True):
            if k <= count:
                return "{} {}".format(size // 2, (size - 1) // 2)
            newspaces[(size - 1) // 2] += count
            newspaces[size // 2] += count
            k -= count
        spaces = newspaces

for task in range(t):
    print("Case #{}: {}".format(task + 1, do_task()))
