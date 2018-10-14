from collections import deque


def reverse_num(n):
    return int(str(n)[::-1])


def get_adjacents(num, end, max_val):
    adjacent = [num + 1]
    rev_num = reverse_num(num)
    if rev_num > num and rev_num <= end and rev_num > max_val:
        adjacent.append(rev_num)
    return adjacent


def bfs(start, end):
    # maintain a queue of paths
    queue = deque()
    # push the first path into the queue
    queue.append([start])
    max_val = start
    while queue:
        # get the first path from the queue
        # print(len(queue))
        path = queue.popleft()
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path
        # and push it into the queue
        for adjacent in get_adjacents(node, end, max_val):
            if adjacent > max_val:
                max_val = adjacent
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def solve(n):
    return len(bfs(1, n))


for case in range(1, int(input()) + 1):
    n = int(input())
    result = solve(n)
    print("Case #{}: {}".format(case, result))
