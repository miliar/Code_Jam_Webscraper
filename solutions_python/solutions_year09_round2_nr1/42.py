

class Node(object):
    def __init__(self, value, name, positive, negative):
        self.value=value
        self.name=name
        self.positive=positive
        self.negative=negative
    def evaluate(self, v, tags):
        v = v * self.value
        if self.name in tags:
            return self.positive.evaluate(v, tags)
        else:
            return self.negative.evaluate(v, tags)
    def __repr__(self):
        return "Node({0},{1},{2},{3})".format(self.value,self.name,self.positive,self.negative)

class NullNode(object):
    def __init__(self, value):
        self.value=value
    def evaluate(self, v, tags):
        return v * self.value

OPEN = object()
CLOSE = object()

class Reader(object):
    def __init__(self, s):
        self.s = s
        self.pos = 0
    def skip_space(self):
        while self.s[self.pos].isspace():
            self.pos+=1
    def get_close_or_tag(self):
        self.skip_space()
        if self.s[self.pos]==")":
            self.pos+=1
            return CLOSE
        # Must be a tag
        startpos = self.pos
        while 1:
            self.pos += 1
            if self.s[self.pos].isspace() or self.s[self.pos]=="(":
                break
        return self.s[startpos:self.pos]
    def get_float(self):
        self.skip_space()
        startpos = self.pos
        while 1:
            self.pos += 1
            if self.s[self.pos].isspace() or self.s[self.pos]==")":
                break
        return float(self.s[startpos:self.pos])
    def get_open(self):
        self.skip_space()
        if self.s[self.pos]=="(":
            self.pos+=1
            return OPEN
        raise Exception("Bad char")
    def get_close(self):
        self.skip_space()
        if self.s[self.pos]==")":
            self.pos+=1
            return CLOSE
        raise Exception("Bad char")

def readtree(reader):
    reader.get_open()
    v = reader.get_float()
    name = reader.get_close_or_tag()
    if name is CLOSE:
        return NullNode(v)
    left = readtree(reader)
    right = readtree(reader)
    reader.get_close()
    return Node(v, name, left, right)

def read_tree_from_stdin():
    lines = int(raw_input().strip())
    treestring = ''.join(raw_input().strip() for i in xrange(lines))
    r = Reader(treestring)
    return readtree(r)

def read_test_case():
    line = raw_input().strip().split(" ")
    return line[2:]

def handle_tests(rootnode):
    numtests = int(raw_input().strip())
    for i in xrange(numtests):
        tags = read_test_case()
        print "{0:.7f}".format(rootnode.evaluate(1.0, tags))

inputs = int(raw_input().strip())
for i in xrange(inputs):
    print "Case #{0}:".format(i+1)
    handle_tests(read_tree_from_stdin())
