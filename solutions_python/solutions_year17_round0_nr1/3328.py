def flip(s):
    ret = ""
    for c in s:
        if c == '+':
            ret += '-'
        else:
            ret += '+'
    return ret


def change(s, k, i):
    return s[: i] + flip(s[i: i + k]) + s[i + k:]


def min_flip(s, k):
    n = len(s)
    start = '+' * n
    if s == start:
        return '0'
    queue = [(start, 0)]
    visited = [start]
    while len(queue) != 0:
        curr, step = queue.pop(0)
        for i in range(0, n - k + 1):
            next = change(curr, k, i)
            if next == s:
                return str(step + 1)
            if next not in visited:
                visited.append(next)
                queue.append((next, step + 1))

    return "IMPOSSIBLE"

output = ""
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S, K = input().split()
        K = int(K)
        output += "Case #" + str(i + 1) + ": " + min_flip(S, K) + "\n"
    print(output)
