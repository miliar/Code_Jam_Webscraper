import queue

def inverse(line, first, length):
    sub = ""
    for i in range(first, first + length):
        if line[i] == '-':
            sub += '+'
        else:
            sub += '-'
    return line[:first] + sub + line[first + length:]

def solve(line, k):
    used = {}
    q = queue.Queue()
    used[line] = 0
    q.put(line)
    while (not q.empty()):
        current = q.get()
        for i in range(0, len(current) - k + 1):
            next_line = inverse(current, i, k)
            if not next_line in used:
                used[next_line] = used[current] + 1
                q.put(next_line)
    return used['+'*len(line)] if '+'*len(line) in used else "IMPOSSIBLE"

if __name__ == "__main__":
    tests = int(input())
    for test in range(tests):
        (line, k) = input().split()
        print("Case #" + str(test + 1) + ": " + str(solve(line, int(k))))

