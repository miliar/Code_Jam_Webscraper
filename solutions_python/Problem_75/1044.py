import sys
from collections import defaultdict
    
class ElementList(object):
    def __init__(self, rules):
        self.clear()
        self.rules = rules
        
    def invoke_seq(self, seq):
        for e in seq:
            self.invoke_elem(e)
    def invoke_elem(self, element):
        # check for combinations
        if self.last != None:
            combo = self.rules.combo[self.last][element]
            if combo != None:
                self.elist[-1] = combo
                self.elements[self.last] -= 1
                if self.elements[self.last] == 0:
                    #print self.rules.opposed[self.last], self.elist
                    try:
                        self.opposed_list.difference_update(self.rules.opposed[self.last])
                        
                    except KeyError:
                        pass
                self.last = combo
                return
        # check for oppositions
        if element in self.opposed_list:
            self.clear()
            return
        # nothing special, just append the element
        self.elist.append(element)
        oppositions = self.rules.opposed[element]
        
        if oppositions:
            self.opposed_list.update(oppositions)
        self.last = element
        self.elements[element] += 1
            
            
    def clear(self):
        self.elements = defaultdict(int)
        self.opposed_list = set()
        self.last = None
        self.elist = [] 

class MagickaRules(object):
    ELEMENTS = 'QWERTASDF'
    def __init__(self, recipes, opposed):
        self.combo = {}
        self.opposed = defaultdict(set)
        self.combo = defaultdict(lambda: defaultdict(lambda: None))

        for o in opposed:
            self.opposed[o[0]].add(o[1])
            self.opposed[o[1]].add(o[0])
       
        for r in recipes:
            self.combo[r[0]][r[1]] = r[2]
            self.combo[r[1]][r[0]] = r[2]
                
def read_test_case(instream):
    items = instream.readline().split()
    C = int(items[0])
    recipes = items[1:C + 1]

    items = items[C + 1:]
    D = int(items[0])
    opposed = items[1:D + 1]
    items = items[D + 1:]

    N = int(items[0])
    invoke = [c for c in items[1]]
    assert N == len(invoke)
    return (recipes, opposed, invoke)

if __name__ == '__main__':
    instream = sys.stdin
    #instream = open("test.1.in", 'r')
    outstream = sys.stdout
    test_cases = int(instream.readline())
    for i in range(test_cases):
        (recipes, opposed, invoke) = read_test_case(instream)
        rules = MagickaRules(recipes, opposed)
        elements = ElementList(rules)
        elements.invoke_seq(invoke)
        outstream.write(('Case #%d: [' % (i + 1)) + ', '.join(elements.elist) + ']\n')
