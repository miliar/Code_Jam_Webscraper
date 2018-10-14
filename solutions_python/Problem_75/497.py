
from sys import argv, exit

if len(argv) < 3:
    exit("Not enough arguments")

input_file = argv[1]
output_file = argv[2]

class magicka(object):
    def __init__(self,parts):
        self.conflicts = set()
        self.maps = {}

        i = 0
        C = int(parts[i])
        i += 1
        for _ in xrange(C):
            self.maps[frozenset(parts[i][:2])] = parts[i][2]
            i += 1

        D = int(parts[i])
        i += 1
        for _ in xrange(D):
            self.conflicts.add(frozenset(parts[i]))
            i += 1

        i += 1
        self.sequence = list(parts[i])


    def calculate(self):
        elements = []
        for s in self.sequence:
            elements.append(s)
            if len(elements) >= 2:
                if frozenset(elements[-2:]) in self.maps:
                    elements = elements[:-2] + list(self.maps[frozenset(elements[-2:])])

                elset = frozenset(elements)

                for s in self.conflicts:
                    if s <= elset:
                        elements = []
                        break

        return str(elements).replace("'",'')



base_elements = set(['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'])
other_elements = set([chr(i) for i in range(ord('A'), ord('Z')+1)]) - base_elements

with open(output_file, 'w') as out_desc:
    in_desc = open(input_file)
    num_cases = int(in_desc.readline().strip())
    for t in xrange(num_cases):



        print >> out_desc, "Case #%d: %s" % (t+1,magicka(in_desc.readline().split()).calculate())

