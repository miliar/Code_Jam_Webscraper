def flip(s, i, k):
    def f(x):
        if i <= x[0] < i + k:
            return '+' if x[1] == '-' else '-'
        return x[1]
    return "".join(map(lambda x: f(x), enumerate(s)))


def isGoal(s):
    return all(map(lambda x: x == '+', s))


def getSuccessors(s, k):
    successors = []
    for i in range(len(s) - k + 1):
        successors.append(flip(s, i, k))
    return successors


def find(s, k):
    if len(s) < k:
        return "IMPOSSIBLE"
    counter = {}
    from collections import deque
    fringe = deque()
    fringe.append((s, 0))
    while len(fringe) != 0:
        state, count = fringe.popleft()
        if isGoal(state):
            return count
        if state not in counter or counter[state] > count:
            counter[state] = count
            for successor in getSuccessors(state, k):
                fringe.append((successor, count + 1))
    return "IMPOSSIBLE"


def main():
    numCases = int(input())
    for i in range(numCases):
        inp = input().split(' ')
        print("Case #{}: {}".format(i + 1, find(inp[0], int(inp[1]))))


if __name__ == "__main__":
    main()
