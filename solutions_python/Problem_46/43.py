import math
import collections
from heapq import heappush, heappop

def successors(state):
    # Return a child-state.
    successors = set()
    for i in range(len(state) - 1):
        # Will we push down?
        if state[i] > state[i + 1]:
            successors.add(swap(state, i, i + 1))
    return successors

def swap(state, i, j):
    copy = list(state)
    copy[i], copy[j] = state[j], state[i]
    return tuple(copy)

def is_goal(state):
    # Check that everyone is <= to index.
    for i in range(len(state)):
        if state[i] > i:
            return False
    return True

def solve_search(root):
    # States are int tuples.
    # Nodes are (swaps, state) tuples.
    expanded = set()
    queue = [root]
    while queue:
        swaps, current = heappop(queue)
        if is_goal(current):
            return swaps
        if current not in expanded:
            expanded.add(current)
            for child in successors(current):
                if child not in expanded:
                    child_swaps = swaps + 1
                    # TODO: add h-value
                    child_node = (child_swaps, child)
                    heappush(queue, child_node)
    print 'No solution found. Uh oh!'
    return None

def heuristic(state, grid, target):
    pass

def last_one(s):
    return len(s.rstrip('0')) - 1


input_file  = 'A-small-attempt0.in'
output_file = 'A-small-attempt0.out.txt'

prob, out = open(input_file), open(output_file, 'w')
cases = int(prob.next().strip())
for i in range(1, cases + 1):
    size = int(prob.next().strip())
    vector = []
    for _ in range(size):
        vector.append(last_one(prob.next().strip()))
    root = (0, tuple(vector))
    solution = solve_search(root)
    print 'Case #%d: %d' % (i, solution)
    out.write('Case #%d: %d\n' % (i, solution))
prob.close()
out.close()
