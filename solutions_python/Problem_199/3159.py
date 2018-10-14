# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import copy


class SearchNode(object):
    def __init__(self, s, n):
        self.name = s
        self.flip = n
        self.turn = 0
        self.nodes = []
        self.prev = None
        self.path = []

    def is_empty(self):
        return not self.nodes

    def add(self, s, n):
        node1 = SearchNode(s, n)
        node1.prev = self
        node1.path = copy.deepcopy(self.path)
        node1.path.append(s)
        node1.turn = copy.deepcopy(self.turn)
        node1.turn += 1
        self.nodes.append(node1)

    def find(self, name):
        for child in range(0, len(self.nodes)):
            if self.nodes[child].name == name:
                return self.nodes[child]

def isGoal(s):
    for i in s:
        if not i:
            return i
    return True

def changeForm(s):
    arr = []
    for i in range(0, len(s)):
        if (s[i] == "+"):
            arr.append(1)
        else:
            arr.append(0)
    return arr

def successor(node):
    arr = []
    current = node.name
    num = node.flip
    for i in range(0, len(current)):
        if not current[i]:
            if (i <= len(current) - num):
                succ1 = copy.deepcopy(current)  # Forward
                for k in range(i, i + num):
                    succ1[k] = not succ1[k]
                if (not arr.__contains__(succ1)) and (not node.path.__contains__(succ1)):
                    arr.append(succ1)
            if (i >= num):
                succ2 = copy.deepcopy(current)  # Backward
                for l in range((i+1) - num, i+1):
                    succ2[l] = not succ2[l]
                if (not arr.__contains__(succ2)) and (not node.path.__contains__(succ2)):
                    arr.append(succ2)
    return arr

def solution(s, n):
    check = 1
    row = changeForm(s)
    if isGoal(row):
        return 0
    queue = []
    initial = SearchNode(row, n)
    initial.path.append(row)
    queue.insert(0, initial)
    beenthere = [initial.name]
    while len(queue) is not 0:
        test = queue.pop(0)
        check += 1
        for next in successor(test):
            if isGoal(next):
                return (test.turn + 1)
            if not beenthere.__contains__(next):
                beenthere.append(next)
                test.add(next, n)
                child = test.find(next)
                queue.append(child) # FIFO :: Breath First Search
    return "IMPOSSIBLE"

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s, n = [r for r in input().split(" ")] # s = String, n = Number of flip per flipper
    print("Case #{}: {}".format(i, solution(str(s), int(n))))

