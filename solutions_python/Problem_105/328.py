import sys
import itertools

class Node(object):
    _nodes = {}

    @classmethod
    def get(cls, k):
        if k not in cls._nodes:
            cls._nodes[k] = cls(k)
        return cls._nodes[k]

    def __init__(self, node_id):
        self._parents = set([])
        self._ancestors = set([])
        self._updated = False
        self._id = node_id

    def add_parent(self, parent):
        self._parents.add(parent)

    def update_ancestors(self):
        queue = []
        queue.extend(self._parents)
        while len(queue):
            ancestor = queue.pop(0)
            self._ancestors.add(ancestor)
            if ancestor._updated:
                self._ancestors.update(ancestor._ancestors)
                continue
            for parent in ancestor._parents:
                queue.append(parent)
        self._ancestors.add(self)
        self._updated = True

    def check(self):
        for (a, b) in itertools.combinations(self._parents, 2):
            if a._ancestors & b._ancestors:
                return True
        return False

    def __repr__(self):
        return "node %d" % self._id


def do_case(k):
    Node._nodes = {}
    f = sys.stdin
    line = f.readline()
    n = int(line.strip())
    for i in xrange(n):
        node = Node.get(i + 1)
        line = f.readline()
        for m in line.strip().split(' ')[1:]:
            child = Node.get(int(m))
            child.add_parent(node)
    for i in xrange(n):
        node = Node.get(i + 1)
        node.update_ancestors()
    for i in xrange(n):
        node = Node.get(i + 1)
        if node.check():
            print 'Case #%d: Yes' % k
            return
    print 'Case #%d: No' % k


def main():
    f = sys.stdin
    line = f.readline()
    T = int(line.strip())
    for i in xrange(T):
        do_case(i + 1)


if __name__ == '__main__':
    main()