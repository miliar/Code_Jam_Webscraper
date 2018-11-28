import fileinput

class case_handler(object):
    def __init__(self, combinations, opposing):
        self.combinations = combinations
        self.opposing = opposing

    def handle_element(self,element_list, cur):
        #print element_list, cur
        if len(element_list) > 0 and tuple(sorted([element_list[-1],cur])) in self.combinations:
            cur = self.combinations[tuple(sorted([element_list[-1],cur]))]
            element_list = element_list[:-1]
        for o in element_list:
            if tuple(sorted([o,cur])) in self.opposing:
                return []
        return element_list + [cur]

def parse_line(l):
    splt = l.split()
    num_comb = int(splt.pop(0))
    combinations = {}
    for i in range(num_comb):
        cur_elem = splt.pop(0)
        combinations[tuple(sorted(cur_elem[:2]))] = cur_elem[2]

    num_opposing = int(splt.pop(0))
    opposing = set()
    for i in range(num_opposing):
        cur_elem = splt.pop(0)
        opposing.add(tuple(sorted(cur_elem)))
    num_invokes = int(splt.pop(0))
    invokes = splt.pop(0)
    assert len(invokes) == num_invokes
    return (combinations, opposing, invokes)
    
def handle_line(i,l):
    (combinations, opposing, invokes) = parse_line(l)
    handler = case_handler(combinations,opposing)
    sol = reduce(handler.handle_element, invokes,[])
    s = "["
    if len(sol) > 0:
        for x in sol[:-1]:
            s = s + x +", "
        s = s + sol[-1]
    s = s + "]"
    print "Case #%d: %s"%(i+1,s)

it = fileinput.input()

num_cases = int(it.next())

for i,l in enumerate(it):
    handle_line(i,l)
