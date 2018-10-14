marked = set()


def adj(k, node):
    l = []
    for i in range(k, len(node)+1):
        flip_amnt = ''.join(["-" if no == "+" else "+" for no in node[i - k:i]])
        prev_flip = node[0:i - k]
        after_flip = node[i:]
        l.append(prev_flip + flip_amnt + after_flip)
    return l


def done(node):
    return sum([1 for c in node if c == "+"]) == len(node)


def bfs(k, start):
    q = [(start, 0)]
    while len(q) != 0:
        node, i = q.pop(0)
        if node in marked:
            continue
        marked.add(node)
        if done(node):
            return i
        for n in adj(k, node):
            if n not in marked:
                q.append((n, i + 1))
    return None

T = int(input())
for t in range(T):
    marked = set()
    line, n = input().split()
    result = bfs(int(n), line)
    result = str(result) if (result is not None) else "IMPOSSIBLE"
    print("Case #" + str(t + 1) + ": " + result)
