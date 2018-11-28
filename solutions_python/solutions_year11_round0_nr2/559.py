import math

class TestCase(object):
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def from_input(cls, input):
        l = input.split()
        index = 0
        combines, opposites, invokes = [], [], []
        
        num_combines = int(l[index])
        index += 1
        for i in range(num_combines):
            combines.append((l[index][:2]+l[index][0], l[index][2]))
            index += 1
        
        num_opposites = int(l[index])
        index += 1
        for i in range(num_opposites):
            opposites.append(l[index]+l[index][0])
            index += 1
        
        num_invokes = int(l[index])
        index += 1
        for i in range(num_invokes):
            invokes.append(l[index][i])
        return cls([combines, opposites, invokes])
    
    def solve(self):
        elements = ""
        for invoke in self.data[2]:
            elements += invoke
            while len(elements) >= 2:
                pre_combine = elements
                elements = self._transform_combines(pre_combine)
                elements = self._transform_opposed(elements)
                if elements == pre_combine:
                    break 
        return "[%s]" % (", ".join(elements))
    
    def _transform_combines(self, elements):
        check = elements[-2:]
        for combine in self.data[0]:
            if check in combine[0]:
                return self._transform_combines(elements[:-2]+combine[1])
        return elements
    
    def _transform_opposed(self, elements):
        check = elements[-1]
        for opposed in self.data[1]:
            if (opposed[0] == check and opposed[1] in elements) or \
               (opposed[1] == check and opposed[0] in elements):
                return ""
        return elements

f = open("magicka.txt", "r")
test_cases = int(f.readline())

for i in range(test_cases):
    test_case = TestCase.from_input(f.readline())
    print "Case #%d: %s" % (i+1, test_case.solve())
