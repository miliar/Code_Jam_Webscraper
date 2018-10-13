import math, sys

class InputError(Exception):
    pass


class Input(object):
    def __init__(self, input_stream):
        self.input_stream = input_stream
        self.__line_words = []
        self.__next_word = None
        self.__num_words = 0
    def _get_line(self):
        return self.input_stream.readline().strip()
    def get_line(self):
        self.__line_words = self._get_line().split()
        self.__num_words = len(self.__line_words)
        self.__next_word = 0

    def read_word(self):
        if self.__next_word == None:
            raise InputError("No words left on the current line")
        word = self.__line_words[self.__next_word]
        self.__next_word += 1
        if self.__next_word >= self.__num_words:
            self.__next_word = None
        return word

    def read_line_list(self, ltype):
        if self.__next_word == None:
            self.get_line()
        result = []
        while True:
            try:
                result.append(ltype(self.read_word()))
            except InputError:
                break
        return result

    def read_line(self, *args):
        if self.__next_word == None:
            self.get_line()
        a = 0
        result = []
        while True:
            try:
                result.append(args[a](self.read_word()))
                if a + 1 < len(args): a += 1
            except InputError:
                break
        if len(result) == 1:
            return result[0]
        return result

    def read_line_into_container(self, container, atype):
        while True:
            try:
                container.append(atype(self.read_word()))
            except InputError:
                break

class DirTree(object):
    def __init__(self):
        self.children = dict()
    def add(self, path):
        pc = path.split('/')
        assert pc[0]==''
        pc = pc[1:]
        node = self.children
        for p in pc:
            if node.has_key(p):
                node = node[p]
            else:
                node[p]=dict()
                node = node[p]
    def add_pending(self, path):
        pc = path.split('/')
        assert pc[0]==''
        pc = pc[1:]
        node = self.children
        for p in pc:
            if node.has_key(p):
                node = node[p]
            elif node.has_key((p, 0)):
                node = node[(p, 0)]
            else:
                node[(p, 0)]=dict()
                node = node[(p, 0)]
    def count_mkdir(self, ddict=None):
        if ddict == None:
            ddict = self.children
        count = 0
        for (k, d) in ddict.iteritems():
            if type(k) == tuple:
                count += 1
            count += self.count_mkdir(d)
        return count




class TestCase(object):
    def __init__(self, input):
        N, M = input.read_line(int, int)
        existing = [input.read_line(str) for n in range(N)]
        pending = [input.read_line(str) for n in range(M)]
        dir_tree = DirTree()
        for e in existing:
            dir_tree.add(e)
        for p in pending:
            dir_tree.add_pending(p)
#        print dir_tree.children
        self.result = "%d"%dir_tree.count_mkdir()



def main():
    input = Input(sys.stdin)
    N = input.read_line(int)
    for n in range(1, N+1):
        sys.stderr.write("case #%d/%d\n"%(n,N))
        case = TestCase(input)
        sys.stdout.write("Case #%d: %s\n"%(n, case.result))

main()








