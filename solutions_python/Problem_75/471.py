#! /usr/bin/python
import sys

base = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    # reading and so
    actual_case += 1
    
    line = sys.stdin.readline()[:-1].split()
    
    c = int(line[0])
    d = int(line[1+c])
    n = int(line[1+c+1+d])
    
    combine = {}
    opposed = dict([(el,[]) for el in base])
    
    for i in [i+1 for i in range(c)]:
        combine[line[i][0] + line[i][1]] = line[i][2]
        combine[line[i][1] + line[i][0]] = line[i][2]
    
    for i in [i+1+c+1 for i in range(d)]:
        opposed[line[i][0]].append(line[i][1])
        opposed[line[i][1]].append(line[i][0])
    
    
    invoked = line[1+c+1+d+1]
    
    result = []
    present = dict([(el,False) for el in base])
    
    for i in range(n):
        current = invoked[i]
        if not result:
           result = [current]
        else:
            if result[-1]+current in combine:
                result[-1] = combine[result[-1]+current]
            else:
                present[result[-1]] = True
                result.append(current)
                for el in opposed[current]:
                    if present[el]:
                        result = []
                        present = dict([(el,False) for el in base])
                        break
    
    res = ", ".join(result)
    print "Case #%d: [%s]" %(actual_case,res)

