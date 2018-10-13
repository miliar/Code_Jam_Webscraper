import queue

EDGE_LENGTH = 1

class Node(object):
    def __init__(self, bits):
        self.id = bits
        self.parent = None

    def __eq__(self, o):
        if type(o) != type(self):
            return False
        if o.id != self.id:
            return False
        return True

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return "(Node %s)" % self.id

    def __repr__(self):
        return "(Node %s)" % self.id

def neighbors(row, masks):
    return [row ^ mask for mask in masks]

def bfs(initial, goal, masks):
    S = set()
    Q = queue.Queue()

    root = Node(initial)
    root.parent = None
    S.add(root)
    Q.put(root)

    while not Q.empty():
        current = Q.get()
        for row in neighbors(current.id, masks):
            if row not in S:
                S.add(row)
                n = Node(row)
                # print("adding row:", n)
                n.parent = current
                if n.id == goal:
                    return n
                else:
                    # print("%s was not goal" % n.id)
                    # print("Goal was: %s" % goal)
                    Q.put(n)

def traversed_length(head):
    edges_traversed = 0
    while head.parent != None:
        head = head.parent
        edges_traversed += 1
    return edges_traversed * EDGE_LENGTH

