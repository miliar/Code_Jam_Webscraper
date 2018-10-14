#!/usr/bin/env python

class Node(object):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}

class DirTree(object):
    def __init__(self):
        self.root = Node("/", None)

    def add(self, dirs):
        # reverse the dirs list for fast pop access and get rid of the root
        rev_dirs = list(reversed(dirs))
        rev_dirs.pop()
        return self._add(self.root, rev_dirs)

    def _add(self, root, dirs):
        if len(dirs) == 0:
            return 0

        dir_name = dirs[-1]
        if dir_name in root.children:
            dirs.pop()
            return self._add(root.children[dir_name], dirs)
        else:
            num_mkdirs = len(dirs)
            curr_node = root
            while len(dirs) > 0:
                curr_dir = dirs.pop()
                next_node = Node(curr_dir, curr_node)
                curr_node.children[curr_dir] = next_node
                curr_node = next_node
            return num_mkdirs

    def print_tree(self):
        self._print_tree(self.root)        

    def _print_tree(self, root):
        path = []
        curr_node = root
        while curr_node != None:
            path.append(curr_node.name)
            curr_node = curr_node.parent
        path.reverse()
        print "Node: " + "/".join(path)
        print root.children
        for child_name in root.children:
            self._print_tree(root.children[child_name])

def readinput(filename):
    f = open(filename, 'r')
    num_tests = int(f.readline())
    test_cases = []
    for i in xrange(num_tests):
        nm = f.readline().split()
        n, m = int(nm[0]), int(nm[1])
        existing_paths = []
        # paths that already exist
        for j in xrange(n):
            existing_paths.append([s.rstrip() for s in f.readline().split("/")])
        create_paths = []
        # paths that we want to create
        for j in xrange(m):
            create_paths.append([s.rstrip() for s in f.readline().split("/")])
        test_cases.append((existing_paths, create_paths))
    return test_cases

def writeoutput(filename, results):
    f = open(filename, 'w')
    for i, result in enumerate(results):
        f.write("Case #%d: %d\n" % ((i+1), result))
    f.close()

def construct_existing_dirs(existing_paths):
    tree = DirTree()
    for path in existing_paths:
        tree.add(path)
    return tree

def calc_num_mkdirs(tree, new_paths):
    num_mkdirs = 0
    for path in new_paths:
        num_mkdirs += tree.add(path)
    return num_mkdirs

def solve(test_case):
    existing_paths, new_paths = test_case
    tree = construct_existing_dirs(existing_paths)
    return calc_num_mkdirs(tree, new_paths)

if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    outfile = sys.argv[2]
    inputs = readinput(infile)
    results = [solve(test_case) for test_case in inputs]
    writeoutput(outfile, results)
