import fileinput
from heapq import heappush, heappop

oppo = lambda x: "+" if x == "-" else "-"


def solve(pancakes, k):
    if k > len(pancakes):
        return 0 if pancakes == "+" * len(pancakes) else "IMPOSSIBLE"
    if k == len(pancakes):
        if pancakes == "+" * len(pancakes):
            return 0
        if pancakes == "-" * len(pancakes):
            return 1
        return "IMPOSSIBLE"

    pancakes = list(pancakes)
    heap = []
    side = 0
    result = 0
    for i, cake in enumerate(pancakes):
        if heap and heap[0] < i:
            heappop(heap)
            side = 1 - side
        if side:
            pancakes[i] = oppo(cake)
            cake = oppo(cake)
        if cake == "-":
            if i + k <= len(pancakes):
                heappush(heap, i + k - 1)
                side = 1 - side
                pancakes[i] = "+"
                result += 1
        # print pancakes, side, heap
    for cake in pancakes:
        if cake == '-':
            return "IMPOSSIBLE"
    return result


f = fileinput.input()
cases = int(f.readline().strip())
for case in range(cases):
    pancakes, k = f.readline().rstrip().split()
    print "Case #{}: {}".format(case + 1, solve(pancakes, int(k)))
