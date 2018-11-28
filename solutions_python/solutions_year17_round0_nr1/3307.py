
from collections import defaultdict

# Priority list
class p_list:

    def __init__(self):
        self.list = []

    def __sort(self):
        self.list.sort(key = lambda state: state[0]) # sort by priority

    def push(self, s, p):
        self.list.append((p, s))
        self.__sort()

    def pop(self):
        obj = self.list[0][1]
        self.list.remove(self.list[0])
        return obj

    def is_empty(self):
        return self.list==[]

# heuristic function; adds cost to number of non-happy pancakes :)
def heuristic(state):
    i = [x for x in state[0] if x == '-']
    return len(i) + state[1]

def goal(state):
    i = [x for x in state[0] if x == '-']
    if len(i) == 0:
        return True

def get_suc(state):
    suc = []
    for i in xrange(0, len(state[0])-state[2]+1):
        s = (state[0], state[1]+1, state[2])
        for j in xrange(i, i+state[2]):
            new = ()
            if s[0][j] == '+':
                new = (s[0][0:j] + '-' + s[0][j+1:], s[1], s[2])
            if s[0][j] == '-':
                new = (s[0][0:j] + '+' + s[0][j+1:], s[1], s[2])
            s = new
        suc.append(s)
    return suc


# perform a* search
def astar_search(start):
    fringe = p_list()
    lkup   = defaultdict(lambda: -1)
    lkup[start[0]] = 1
    fringe.push(start, heuristic(start))
    while not fringe.is_empty():
        s = fringe.pop()
        if goal(s):
            return s[1]
        suc = get_suc(s)
        for i in suc:
            if lkup[i[0]] != -1:
                pass
            else:
                lkup[i[0]] = 1;
                fringe.push(i, heuristic(i))
    return "IMPOSSIBLE"


# Read input using raw_input()
t = int(raw_input())

for i in xrange(1, t+1):
    st, k = [s for s in raw_input().split(' ')];
    k = int(k)
    res = 0
    if k > len(st):
         res = "IMPOSSIBLE"
    else:
        state0 = (st, 0, k)
        res = astar_search(state0)
    print "Case #{}: {}".format(i, res)
