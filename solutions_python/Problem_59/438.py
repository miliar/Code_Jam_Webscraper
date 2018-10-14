import sys


class directory(object):
    
    def __init__(self, parent, name, children={}):
        self.parent = parent
        self.name = name
        if children:
            self.children = children
        else:
            self.children = {}
    
num_cases = int(sys.stdin.readline())


def add_dirs(parent, dirs):
    if dirs:
        current_dir_name = dirs.pop(0)
        current_dir = parent.children.get(current_dir_name)
        if current_dir is None:
            current_dir = directory(parent, current_dir_name)
            parent.children[current_dir_name] = current_dir
            return 1 + add_dirs(current_dir, dirs)
        else:
            return add_dirs(current_dir, dirs)
    else:
        return 0


def get_num_ops(n, m, existing, wanted):
    root = directory(None, 'root')
    
    for path in existing:
        dirs = path.strip('/').split('/')
        add_dirs(root, dirs)
    
    num_ops = 0
    for path in wanted:
        dirs = path.strip('/').split('/')
        num_ops += add_dirs(root, dirs)

    return num_ops


for j in xrange(num_cases):
    n, m = [int(e) for e in sys.stdin.readline().split()]

    existing = []
    for i in xrange(n):
        existing.append(sys.stdin.readline().strip())
    
    wanted = []
    for i in xrange(m):
        wanted.append(sys.stdin.readline().strip())
        
    print "Case #%s: %s" % (j+1, get_num_ops(n, m, existing, wanted))
    j += 1
