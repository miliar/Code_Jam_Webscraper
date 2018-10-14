import fileinput
from queue import Queue


def flip(S):
    def opposite(e):
        if e == '+':
            return '-'
        else:
            return '+'

    return ''.join([opposite(s) for s in S ])


def neighbours(S, K):
    n = []
    for i in range(len(S) - K + 1):
        n.append(S[:i] + flip(S[i: i + K]) + S[i + K:])

    return n


def isPossible(S, K):
    visited = set()
    queue = Queue()
    depthQueue = Queue()

    depthQueue.put(0)
    queue.put(S)
    visited.add(S)

    while not queue.empty():
        current = queue.get()
        depth = depthQueue.get()

        if current.count('+') == len(current): #all happy
            return depth
        else:
            adjacent = neighbours(current, K)
            for node in adjacent:
                if node not in visited:
                    visited.add(node)
                    queue.put(node)
                    depthQueue.put(depth + 1)

    return 'IMPOSSIBLE'

t = int(input()) 
for i in range(1, t + 1):
	L = input().split(' ')
	S = str(L[0])
	K = int(L[1])
	result = isPossible(S,K)
	print("Case #{}: {}".format(i, result))




