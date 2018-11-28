#!/usr/bin/env python
from sys import argv

def solve(case):
    d = {}
    with open("dict.txt", 'r') as f:
        lines = f.readlines()
    for i in range(0, len(lines), 2):
        c1 = lines[i].rstrip("\n")
        c2 = lines[i + 1].rstrip("\n")
        d[c1] = c2
    print d
    result = ""
    g = case["g"]
    for c in g:
        result = result + d[c]
    return [result]

def read_case(lines):
    g = lines.pop(0).rstrip("\n")
    return {"g": g}

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