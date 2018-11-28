import re

class Problem:

    input = None
    output = None

    # search engines list
    engines = []
    num_engines = 0
    # queries list
    queries = []
    num_queries = 0

    def read_vector(self):
        l = self.input.readline().split()
        return l

    def read_int_vector(self):
        l = self.input.readline().split()
        l = [int(x) for x in l]
        return l

    def read_matrix(self, num_rows):
        m = []
        for i in range(num_rows):
            l = self.input.readline().split()
            m.append(l)
        return m

    def read_int_matrix(self, num_rows):
        m = []
        for i in range(num_rows):
            l = self.input.readline().split()
            l = [int(x) for x in l]
            m.append(l)
        return m

    def read_list(self, num_rows):
        l = []
        for i in range(num_rows):
            l.append(self.input.readline())
        return l

    def read_int_list(self, num_rows):
        l = []
        for i in range(num_rows):
            l.append(int(self.input.readline()))
        return l

    """ """

    def run(self):
        self.input = open("A.in", "r")
        self.output = open("A.out",  "w")

        nums = self.read_int_vector()
        num_letters = nums[0]
        num_words = nums[1]
        num_patterns = nums[2]

        words = []
        for i in range(num_words):
            print 'word ' + str(i) + '\n'
            words.append(self.read_vector()[0])

        for i in range(num_patterns):
            print 'word ' + str(i) + '\n'
            p = self.read_vector()[0]
            p = p.replace('(', '[')
            p = p.replace(')', ']')
            p = '^' + p + '$'
            p = re.compile(p)
            result = 0
            for w in words:
                if p.match(w):
                    result += 1
            self.output.write('Case #' + str(i+1) + ': ' + str(result) + '\n')
            

        self.input.close()
        self.output.close()

    def solve(self):
        r = 0
        ces = self.engines[:]

        for e in self.queries:
            if (len(ces)==1) and (e in ces):
                print str(self.engines) + '++\n'
                r+=1
                ces = self.engines[:]

            if e in ces:
                ces.remove(e)

        return r

p = Problem()
p.run()