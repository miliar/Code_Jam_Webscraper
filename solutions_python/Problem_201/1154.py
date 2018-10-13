import math
import sys

def next_line(f):
    line = f.readline()
    if line[-1] == '\n':
        line = line[:-1]
    return line.split(' ')

class Element:
    def __init__(self, value, n=1):
        self.value = value
        self.n = n

    def split(self):
        high = int(math.ceil((self.value-1)/2.))
        low = int(math.floor((self.value-1)/2.))

        if high == low:
            return [Element(high, 2*self.n)]

        return [Element(high, self.n), Element(low, self.n)]

    def __str__(self):
        return '%d[x %d]' % (self.value, self.n)

class List:
    def __init__(self, elements, exponent=0):
        self.elements = elements
        self.exponent = exponent

    def __split(self):
        new_list = []
        for element in self.elements:
            aux_elements = element.split()
            first = aux_elements[0]
            if new_list and new_list[-1].value == first.value:
                new_list[-1].n = new_list[-1].n + first.n
            else:
                new_list += [first]
            if len(aux_elements) > 1:
                new_list += aux_elements[1:]

        return List(new_list, self.exponent+1)

    def __k(self):
        return pow(2, self.exponent)

    def __next_k(self):
        return pow(2, self.exponent+1)

    def get(self, position):
        l = self
        while(position >= l.__next_k()):
            l = l.__split()

        acum = l.__k()
        for element in l.elements:
            acum += element.n
            if acum > position:
                return element.value


with open(len(sys.argv) > 1 and sys.argv[1] or 'input/C-small-2-attempt0.in', 'r') as f:
    n_cases = int(next_line(f)[0])
    for case in range(1, n_cases+1):
        N_str, K_str = next_line(f)
        l = List([Element(int(N_str))])
        gap_size = l.get(int(K_str))
        print("Case #%d: %s %s" % (case, int(math.ceil((gap_size-1)/2.)), int(math.floor((gap_size-1)/2.))))

