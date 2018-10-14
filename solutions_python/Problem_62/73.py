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



class TestCase(object):
    def __init__(self, input):
        N = input.read_line(int)
        A, B = list(), list()
        #need to find wires whose intervals overlap.
        # wires a1,b1, a1,b2 overlap iff
        # a1 < a2 and b1 > b2 or a1 > a2 and b1 < b2
        # for a given interval a1,b1, find all intervals with a1>a2 and b1<b2
        for i in range(N):
            a, b = input.read_line(int, int)
            A.append(a)
            B.append(b)
        count = 0
        for i in range(N):
            for j in range(i+1, N):
                if A[i]<A[j] and B[i]>B[j]:
                    count +=1
                elif A[i]>A[j] and B[i]<B[j]:
                    count +=1

        self.result = "%d"%count




def main():
    input = Input(sys.stdin)
    N = input.read_line(int)
    for n in range(1, N+1):
        sys.stderr.write("case #%d/%d\n"%(n,N))
        case = TestCase(input)
        sys.stdout.write("Case #%d: %s\n"%(n, case.result))

main()








