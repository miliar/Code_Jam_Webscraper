case_prefix = 'Case #'

class Node:
    value = str()
    children = set()

    def __init__(self, value):
        self.value = value
        self.children = set()

    def getChild(self, value):
        for c in self.children:
            if c.value == value:
                return c
        return None

    def addChild(self, childNode):
        self.children.add(childNode)

    def __str__(self):
        return 'value: '+self.value+' children: ' + str(len(self.children))

def traverse_tree(root):
    s = root.value + ' children:[ '
    for c in root.children:
        s = s + ' ' + traverse_tree(c)
    s = s + ' ]'
    return s

def build_result_string(case_num, verdict):
    return case_prefix + str(case_num) + ': ' + verdict


def getCostAndNextNode(root, dir_name):
    cost = 0
    matching_child = root.getChild(dir_name)
    if matching_child == None:
        # add new child
        matching_child = Node(dir_name)
        root.addChild(matching_child)
        cost = 1
    return (cost, matching_child)

def add_to_tree(root, path):
    #print root, path
    num_slashes = path.count('/')
    if num_slashes == 0:
        # deal with child
        (cost, matching_child) = getCostAndNextNode(root, path)
        return cost
    slash_index = path.index('/')
    dir_name = path[:slash_index]
    remaining_path = path[slash_index+1:]
    (cost, matching_child) = getCostAndNextNode(root, dir_name)
    return cost + add_to_tree(matching_child, remaining_path)

def build_tree(root, lines):
    if root == None:
        root = Node('')
    cost = 0
    for line in lines:
        path = line.strip()
        path = path[1:]
        cost = cost + add_to_tree(root, path)
    #print traverse_tree(root)
    return root, cost

f = open('A-large.in', 'r')
num_tests = int(f.readline().strip())

for case in range(num_tests):
    (num_exist, num_create) = (long(t) for t in f.readline().strip().split())
    #print num_exist, num_create
    existing = list()
    for i in range(num_exist):
        existing.append(f.readline().strip())
    create = list()
    for i in range(num_create):
        create.append(f.readline().strip())
    root, cost = build_tree(None, existing)
    root, cost = build_tree(root, create)
    print build_result_string(case+1, str(cost))    
