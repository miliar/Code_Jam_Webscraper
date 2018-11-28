from collections import deque

def flip(seq, a, b):
    flip_region = "".join(["+" if x == "-" else "-" for x in seq[a:b]])
    new_seq = seq[:a] + flip_region + seq[b:]
    return new_seq

def BFS(seq:str, k:int):
    Q = deque()
    visited = set()
    Q.append((seq, 0))
    visited.add(seq)
    while Q:
        seq, depth = Q.popleft()
        if "-" not in seq:
            return depth
        for start in range(len(seq) - k + 1):
            end = start + k
            new_seq = flip(seq, start, end)
            if new_seq in visited:
                continue
            visited.add(new_seq)
            Q.append((new_seq, depth+1))


if __name__ == "__main__":
    with open("inp.txt", "r") as f:
        n = f.readline()
        for i in range(1, int(n)+1):
            seq, k = map(str, f.readline().split())
            ans = BFS(seq, int(k))
            if ans is None:
                ans = "IMPOSSIBLE"
            print("Case #%d: %s" % (i, ans))
