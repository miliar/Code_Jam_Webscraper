def interpret(s):
    l = []
    for c in s:
        b = True if c == '+' else False
        l.append(b)
    return l

def success(l):
    for b in l:
        if not b: return False
    return True

def main(s, k):
    l = interpret(s)
    count = 0
    for i in range(len(l) - k + 1):
        if not l[i]:
            for j in range(i, i + k):
                l[j] = not l[j]
            count += 1
    if success(l): return count
    else: return "IMPOSSIBLE"

t = int(input())
for i in range(1, t + 1):
    s, k = input().split(" ")
    k = int(k)
    print("Case #{}: {}".format(i, main(s, k)))
