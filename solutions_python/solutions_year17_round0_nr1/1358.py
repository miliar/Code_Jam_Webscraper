n = int(input())
cases = []
for _ in range(n):
    case, size = input().split()
    size = int(size)
    case = list(map(lambda x: x == "+", case))
    cases.append((case, size))


def to_string(case):
    return "".join(map(lambda x: "+" if x else "-", case))


def solve(case, size):
    current = case[:]
    count = 0
    while True:
        while current and current[0]:
            current.pop(0)
        if not current:
            return count
        if len(current) < size:
            return "IMPOSSIBLE"
        for i in range(size):
            current[i] = not current[i]
        count += 1


if __name__ == "__main__":
    for index, (case, size) in enumerate(cases):
        print("Case #{}: {}".format(index+1, solve(case, size)))
