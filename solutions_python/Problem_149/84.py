from doctest import testmod
import collections

class Tree(object):
    def __init__(self, data):
        self.data = data
        self.data_size = 1

    @staticmethod
    def make_tree(lst):
        if len(lst) == 0: return None
        else:
            mid = len(lst) / 2
            data = lst[mid]
            t = Tree(data)
            left = Tree.make_tree(lst[:mid])
            right = Tree.make_tree(lst[mid + 1:])

            t.left = left
            t.right = right
            t.size = Tree.tree_size(left) + Tree.tree_size(right) + 1
            return t

    @staticmethod
    def tree_size(self):
        if self is None:
            return 0
        return self.size

    def less_than(self, elt):
        if self.data < elt:
            return self.right.less_than(elt) + self.data_size + Tree.tree_size(self.left)
        elif self.data > elt:
            return self.left.less_than(elt)
        else:
            return self.data_size + Tree.tree_size(self.left)

    def greater_than(self, elt):
        if self.data > elt:
            return self.left.greater_than(elt) + self.data_size + Tree.tree_size(self.right)
        elif self.data < elt:
            return self.right.greater_than(elt)
        else:
            return self.data_size + Tree.tree_size(self.right)

    def remove(self, elt):
        if self.data == elt:
            self.data_size = 0
        elif self.data < elt:
            self.right.remove(elt)
        else:
            self.left.remove(elt)
        self.size = Tree.tree_size(self.left) + Tree.tree_size(self.right) + self.data_size

    def __str__(self):
        return "[%s, %s, %s]" % (str(self.left), self.data, self.right)

def solve_up_and_down(lst):
    index_tree = Tree.make_tree(list(range(len(lst))))
    sorted_list = sorted(lst)

    indices = {}
    for i in range(len(lst)):
        indices[lst[i]] = i

    sorted_indices = [indices[x] for x in sorted_list]

    return up_and_down_cost(sorted_indices, index_tree, 0)

def up_and_down_cost(indices, index_tree, i):
    if i >= len(indices): return 0

    pos = indices[i]
    index_tree.remove(pos)
    cost = min(index_tree.less_than(pos), index_tree.greater_than(pos))

    return cost + up_and_down_cost(indices, index_tree, i + 1)

def main():
    with open(IN_FILE) as f:
        cases = int(f.readline()[:-1])
        for case in range(cases):
            _ = f.readline()
            lst = [int(x) for x in f.readline()[:-1].split()]
            print "Case #%s: %s" % (case + 1, solve_up_and_down(lst))

IN_FILE = 'test.in'
OUT_FILE = 'solution.out'

if __name__ == '__main__':
    main()
