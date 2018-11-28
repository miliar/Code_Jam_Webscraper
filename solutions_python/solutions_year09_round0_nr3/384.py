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

    def read_line(self):
        l = self.input.readline()
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
        self.input = open("C.in", "r")
        self.output = open("C.out",  "w")

        letters = {
            'w': [0],
            'e': [1, 6, 14],
            'l': [2],
            'c': [3, 11],
            'o': [4, 9, 12],
            'm': [5,18],
            ' ': [7, 10, 15],
            't': [8],
            'd': [13],
            'j': [16],
            'a': [17],
        }

            
        num_strings = self.read_int_vector()[0]
 
        for i in range(num_strings):
            cases = []
            for j in range(19):
                cases.append(0)
            print 'string ' + str(i) + '\n'
            s = self.read_line()
            for l in s:
                if l in letters:
                    print l
                    for place in letters[l]:
                        if place == 0:
                            cases[place] += 1
                        else:
                            cases[place] += cases[place-1]

            print cases[18]
            result = cases[18] % 10000
            self.output.write('Case #%d: %04d \n' % (i+1, result))
            

        self.input.close()
        self.output.close()


p = Problem()
p.run()