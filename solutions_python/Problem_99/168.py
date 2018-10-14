#!/usr/bin/env python
from sys import argv
from operator import mul

def solve(a, b, p):
    result = 0
    
    k_keep = 0 # Keystrokes if I keep typing 
    k_back = []  # Keystrokes if I press backspace list
    k_enter = 0 # Keystrokes if I press enter right away    7    7    7    7    7
    k_all = a + b + 1# if erased all 
    
    k_enter = b + 2
    
    p1 = reduce(mul, p)
    k_keep = p1 * (b - a + 1) + (1 - p1) * (2 * b - a + 2)
    
    
    for i in range(1, a):
        key_correct = 2 * i + (b - a + 1) 
        key_incorrect = key_correct + b + 1
        p1 = p1 / p[a - i]
        k_back.append(p1 * key_correct + (1 - p1) * key_incorrect)
       
    print k_keep, k_all, k_enter, k_back,
    if len(k_back) > 0:
        result = min ([k_keep, k_all, k_enter, min(k_back)])
    else:
        result = min ([k_keep, k_all, k_enter])
    
    return result

def read_case(lines):
    line = lines.pop(0)
    a, b = [int(x) for x in line.split(" ")]
    line = lines.pop(0)    
    p = [float(x) for x in line.split(" ")]
    return (a, b, p)

def result2str(i, result):
    s = "Case #" + str(i) + ": "
    s = s + str(result)
    # " ".join([str(i) for i in result])
    return s 
    
def main(in_filename, out_filename):
    with open(in_filename, 'r') as f:
        lines = f.readlines()

    n = int(lines.pop(0))
    output = []
    for i in range(1, n + 1):
        case = read_case(lines)
        result = solve(*case)
        s = result2str(i, result)
        print s
        output.append(s + "\n")

    with open(out_filename, 'w') as f:
        f.writelines(output)
   
        
if __name__ == '__main__':
    main(argv[1], argv[2])