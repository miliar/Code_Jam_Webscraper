from queue import PriorityQueue

def solve():
    n, k = map(int, input().split(" "))
    q = PriorityQueue()
    q.put(-n)
    for _ in range(k-1):
        s = -q.get()
        q.put(-(s // 2))
        if s % 2:
            q.put(-(s // 2))
        else:
            q.put(-int(s / 2 - 1))
    s = -q.get()
    mx = s // 2
    mn = mx + s % 2 - 1
    return f"{mx} {mn}"

for case in range(int(input())):
    print(f"Case #{case + 1}: {solve()}")
