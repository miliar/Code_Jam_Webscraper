import os, string
from itertools import izip

# just to make sure I read the file from the correct directory
if len(os.path.dirname(__file__)) > 0:
    os.chdir(os.path.dirname(__file__))


in_file = r"A-large.in"
out_file = r"out.txt"


def build_test_case(line):
    line = line.strip().split(" ")
    O = []
    B = []
    alt = []
    # Each test case consists of a single line beginning with a positive integer N the number of buttons that need to be pressed
    for i in range(1,len(line),2):
        alt.append(line[i])
        if line[i] == "O":
            O.append(int(line[i+1]))
        else:
            B.append(int(line[i+1]))
    return (O,B,alt)
    
def solve_test_case(O, B, alt):
    O = [1 + abs(x[1] - x[0]) for x in izip([1] + O, O)]
    B = [1 + abs(x[1] - x[0]) for x in izip([1] + B, B)]
    d = {"O" : O, "B" : B}
    last_robot = None
    last_seq_len = 0
    total = 0
    for robot in alt:
        steps = d[robot][0]
        if robot != last_robot:
            steps = max(1, steps - last_seq_len)
            last_seq_len = 0
            last_robot = robot
        total += steps
        last_seq_len += steps
        d[robot] = d[robot][1:]
    return total

def write_test_case(outf, testn, res):
    s = "Case #%d: %d\n" % (testn,res)
    outf.write(s)
    

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