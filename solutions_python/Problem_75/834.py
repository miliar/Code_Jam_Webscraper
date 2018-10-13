
class wizard(object):
    def __init__(self, combine, opposed):
        self.elements = ""
        self.opposed = opposed
        self.pairs = {}
        for base_pair in combine:
            self.pairs[base_pair[:2]] = base_pair[2]
        
    def invoke(self, element):
        self.elements += element
        self.reaction(element)
                   
    def reaction(self, elements):
        reaction1 = self.pairs.get(self.elements[-2:])
        reaction2 = self.pairs.get(self.elements[:-3:-1])
        
        action = max(reaction1, reaction2)
        
        if action:
            self.elements = self.elements[:-2] + action
            
        else:
            for o in self.opposed:
                if self.has_clear_elem(o):
                    self.elements = ""
                    return
            
    def has_clear_elem(self, o):
        if (self.elements[-1] == o[0] and o[1] in self.elements or
            self.elements[-1] == o[1] and o[0] in self.elements):
            return True
    
        
def formatting(string):
    out = []
    for char in string:
        out.append(char)
    return "[" + ", ".join(out) + "]"
        
        
        
        
def test_sequence(line):
    split = line.split()
    combine = split[1:int(split[0])+1]
    opposed = split[int(split[0])+2:-2]
    invoke = split[-1]
    
    w = wizard(combine, opposed)
    for elem in invoke:
        w.invoke(elem)
    return formatting(w.elements)


if __name__ == "__main__":
    
    
    name = raw_input("Input file:")
    input_file = open(name + ".in")
    output_file = open(name + ".txt", "w")
    input_file.readline()
    line = input_file.readline()
    case = 1
    while line:
        output_file.write("Case #%d: %s\n" %(case, test_sequence(line)))
        line = input_file.readline()
        case += 1
    input_file.close()
    output_file.close()
