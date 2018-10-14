import re

class Problem:

    input = None
    output = None

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
        self.input = open("A.in", "r")
        self.output = open("A.out",  "w")

        weights = {}

        num_tests = self.read_int_vector()[0]

        for i in range(num_tests):
            weights = {}

            num = self.read_vector()[0]

            #if len(num) == 1:
            #    self.output.write('Case #%d: %d \n' % (i+1, 0))
            #    continue

            w = 1
            for d in num:
                if (d not in weights):
                    weights[d] = w
                    if w==1:
                        w = 0
                    elif w==0:
                        w = 2
                    else:
                        w+=1
            res = 0
            base = len(weights)
            if base == 1:
                base = 2
            p = len(num)
            for d in num:
                p -= 1
                res += weights[d]*pow(base, p)

            self.output.write('Case #%d: %d \n' % (i+1, res))


        self.input.close()
        self.output.close()


p = Problem()
p.run()