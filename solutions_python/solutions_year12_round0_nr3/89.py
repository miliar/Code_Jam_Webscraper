#!/usr/bin/env python
from sys import argv

def solve(case):
    a = case["a"]
    b = case["b"]
    result = 0
    for n in range (a, b + 1):
    #for n in range(a, a + 2):
        s = str(n)
        l = []
        for p in range(1, len(s)):
            m = int(s[p:] + s[:p])
            if (m >= a) and (m <= b) and (m > n):
                if m in l:
                    continue
                else:
                    l.append(m)
                    result = result + 1
    
    return [result]

def read_case(lines):
    s = lines.pop(0).split(" ")
    p = [int(x) for x in s]
    a = p[0]
    b = p[1]
    return {"a": a, "b": b}

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