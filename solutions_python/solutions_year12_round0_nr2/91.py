#!/usr/bin/env python
from sys import argv

# not strange
fl = {}
# strange
sl = {}

for c1 in range(0, 11):
    for c2 in range(max(c1 - 2,0), min(c1 + 3, 11)):
        for c3 in range(c1, c2 + 1):
            b = c1 + c2 + c3
            print b, c1, c2, c3
            if abs(c2 - c1) < 2:
                fl[b] = max(c1,c2)
            else:
                sl[b] = max(c1,c2)
print sl
    
def solve(case):
    result = 0
    n = case["n"]
    s = case["s"]
    p = case["p"]
    t = case["t"]
    print case
    
    for i in t:
        if fl.get(i, -1) >= p:
            result = result + 1
        else:
            if s > 0:
                if sl.get(i, -1) >= p:
                    s = s - 1
                    result = result + 1 
    return [result]

def read_case(lines):
    line = lines.pop(0)
    s = line.split(" ")
    ints = [int(x) for x in s]
    n = ints[0]
    s = ints[1]
    p = ints[2]
    t = ints[3:]
    return {"n": n, "s": s, "p": p, "t": t}

def result2str(i, result):
    s = "Case #" + str(i) + ": "
    s = s + " ".join([str(i) for i in result])
    return s 
    
def main(in_filename, out_filename):
    with open(in_filename, 'r') as f:
        lines = f.readlines()

    n = int(lines.pop(0))
    output = []
    for i in range(1, n + 1):
        case = read_case(lines)
        result = solve(case)
        s = result2str(i, result)
        print s
        output.append(s + "\n")

    with open(out_filename, 'w') as f:
        f.writelines(output)
   
        
if __name__ == '__main__':
    main(argv[1], argv[2])