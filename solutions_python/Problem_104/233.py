#!/usr/bin/env python
from sys import argv

def solve(n, s):
    result1 = []
    result1 = []
    all_sums = []
    all_sums.append({})
    for i in s:
        all_sums[0][i] = [i]
    
    for c in range(1, n):
        sums = {}
        for sum, items in all_sums[c - 1].items():
            for i in s:
                if i not in items:
                    sum2 = sum + i
                    items2 = items[:]
                    items2.append(i)
                    for j in range(0, c):
                        if all_sums[j].has_key(sum2):
                            return (all_sums[j][sum2], items2)
                    sums[sum2] = items2
               
        all_sums.append(sums)
    return "Impossible"

def read_case(lines):
    line = lines.pop(0)
    l = [int(x) for x in line.split(" ")]
    n = l[0]    
    s = l[1:]
    return (n, s)

def result2str(i, result):
    s = "Case #" + str(i) + ": "
    if result == "Impossible":
        s = s + result
    else:
        s = s + "\n"  + " ".join([str(i) for i in result[0]])
        s = s + "\n"  + " ".join([str(i) for i in result[1]])
    #s = s + str(result)
    # " ".join([str(i) for i in result])
    return s 
   
    
def main(in_filename, out_filename):
    with open(in_filename, 'r') as f:
        lines = f.readlines()

    n = int(lines.pop(0))
    cases = []
    for i in range(1, n + 1):
        case = read_case(lines)
        cases.append((i, case))
        
    output = []
    for case in cases:
        result = solve(*case[1])
        s = result2str(case[0], result)
        print s
        output.append(s + "\n")
            
    with open(out_filename, 'w') as f:
        f.writelines(output)
        
if __name__ == '__main__':
    main(argv[1], argv[2])