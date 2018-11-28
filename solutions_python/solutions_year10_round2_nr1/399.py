import sys

class Reader:
    def __init__(self, filename):
        self.fp = open(filename)

    def read(self):
        tokens = self.fp.readline().split()
        result = []
        for token in tokens:
            try:
                result.append(int(token, 10))
            except ValueError:
                result.append(token)
        return result

class Node:
    def __init__(self):
        self.children = {}

class FileSystem:
    def __init__(self):
        self.count = 0 
        self.root = Node()
        
    def learn(self, path, count=True):
        if isinstance(path, str):
            assert path[0] == '/'
            path = path[1:].split('/')
        node = self.root
        for part in path:
            if part not in node.children:
                node.children[part] = Node()
                if count:
                    self.count += 1
            node = node.children[part]

if __name__ == '__main__':
    reader = Reader(sys.argv[1])
    case_count, = reader.read()
    for case in xrange(case_count):
        existing_count, new_count = reader.read()
        fs = FileSystem()
        for i in xrange(existing_count):
            path, = reader.read()
            fs.learn(path, count=False)
        for i in xrange(new_count):
            path, = reader.read()
            fs.learn(path, count=True)
        print "Case #%d: %d" % (case + 1, fs.count)
