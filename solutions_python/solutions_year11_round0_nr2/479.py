import string, os

# just to make sure I read the file from the correct directory
if len(os.path.dirname(__file__)) > 0:
    os.chdir(os.path.dirname(__file__))


in_file = r"B-large.in"
out_file = r"q2_large_out.txt"

class SuperCounter:
    def __init__(self):
        self.dict = {}
        self.set = set()
    def add(self,v):
        self.dict[v] = self.dict.setdefault(v,0) + 1
        self.set.add(v)
    def subscract(self,v):
        c = self.dict.get(v,0)
        if c > 1:
            self.dict[v] = c - 1
        if c == 1:
            del(self.dict[v])
            self.set.remove(v)
    def clear(self):  
        self.dict = {}
        self.set.clear()
    def contains_any(self, other_set):
        return len(self.set.intersection(other_set)) > 0
            


def build_test_case(line):
    combs = {}
    opps = {}
    line = line.strip().split(" ")
    # First an integer C, followed by C strings
    C = int(line[0])
    for c in line[1:C+1]:
        combs[ c[:2] ] = c[2]
        combs[ c[1] + c[0]] = c[2]
    # Next will come an integer D, followed by D strings
    line = line[C+1:]
    D = int(line[0])
    for d in line[1:D+1]:
        opps.setdefault(d[0], set()).add(d[1])
        opps.setdefault(d[1], set()).add(d[0])
    line = line[D+1:]
    # Finally there will be an integer N, followed by a single string containing N
    in_seq = [c for c in line[1]]
    return (combs,opps,in_seq)
    
def write_test_case(outf, testn, res):
    s = "Case #%d: [%s]\n" % (testn, string.join(res, ", "))
    outf.write(s)
    
def solve_test_case(combs,opps,in_seq):
    res = []
    res_set = SuperCounter()
    def add_to_res(c):
        res.append(c)
        res_set.add(c)
    def replace_last(c):
        res_set.subscract(res[-1])
        res_set.add(c)
        res[-1] = c
        
    for c in in_seq:
        if len(res) == 0:
            add_to_res(c)
        else:
            s = res[-1] + c
            if combs.has_key(s):
                replace_last(combs[s])
            elif res_set.contains_any(opps.get(c,[])):
                res = []
                res_set.clear()
            else:
                add_to_res(c)
    return res
            


def read_input():
    with open(out_file, "w") as outf:
        with open(in_file) as f:
            # The first line of the input gives the number of test cases, T.
            T = int(f.readline().strip())
            for i in xrange(0,T):
                print "working on case ", i
                case = build_test_case(f.readline())
                res = solve_test_case(*case)
                write_test_case(outf, i+1, res)

read_input()                
                    
                