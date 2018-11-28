# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 07:00:45 2017

@author: Bert
"""



def handle_case(rows,R,C):
    original = [list(r) for r in rows]
    new = [list(r) for r in rows]
    char = ''
        
    #vertical
    for r in range(R):
        for c in range(C):
            if original[r][c] != "?" and original[r][c] != "*":
                char = original[r][c]
                for i in range(R):
                    if original[i][c] == "*":
                        continue
                    elif original[i][c] == "?" or original[i][c] == char:
                        new[i][c] = char
                        original[i][c] = "*"
                    else:
                        break
    #horizontal
    for r in range(R):
        for c in range(C):
            if original[r][c] != "?" and original[r][c] != "*":
                char = original[r][c]
                for j in range(C):
                    if original[r][j] == "*":
                        continue
                    elif original[r][j] == "?" or original[r][j] == char:
                        new[r][j] = char
                        original[r][j] = "*"
                    else:
                        break
    #for case 6 et al.
    edges = 0
    for c in range(C):
        if new[0][c] == "?":
            count = 0
            for r in range(R):
                if new[r][c] == "?":
                    count += 1
            if count == R:
                edges += 1
    
    if edges > 0:
        original = [[i for i in r] for r in new]

        #horizontal
        for r in range(R):
            for c in range(C):
                if original[r][c] != "?" and original[r][c] != "*":
                    char = original[r][c]
                    for j in range(C):
                        if original[r][j] == "*":
                            continue
                        elif original[r][j] == "?" or original[r][j] == char:
                            new[r][j] = char
                            original[r][j] = "*"
                        else:
                            break
#                
    return new
    


#with open("A-small.in") as fh, open("output-small.txt","w") as op:
with open("A-large.in") as fh, open("output-Alarge.txt","w") as op:
#with open("Atest.txt") as fh, open("output-test.txt","w") as op:
    cases = int(fh.readline())
    for x in range(cases):
        R,C = fh.readline().split()
        rows = []
        for i in range(int(R)):
            line = []
            lin = fh.readline()
            for j in range(int(C)):
                line.append(lin[j])
            rows.append(line)
        solution = handle_case(rows,int(R),int(C))
        o = "Case #{}:".format(x+1)
        print (o)
        op.write(o)
        op.write("\n")
        for r in solution:
            o = "".join(r)
            print (o)
            op.write(o)
            op.write("\n")