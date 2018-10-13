t = int(input())


def problem(i):
    inp = input().split()
    stack = inp[0]
    k = int(inp[1])
    count = 0
    while True:
        if '-' not in stack:
            return count
        start = stack.index("-")
        if start > (len(stack) - k):
            return "IMPOSSIBLE"
        stack = flip(stack, start, k)
        count += 1


def flip(stack, start, k):
    return stack[:start] + ''.join([('+', '-')[n == '+'] for n in stack[start:start+k]]) + stack[start+k:]

for i in range(1, t + 1):
    print("Case #{}: {}".format(i, problem(i)))
