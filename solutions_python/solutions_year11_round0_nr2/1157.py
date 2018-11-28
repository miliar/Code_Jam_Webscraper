import re

with open("input.txt",'r') as infile:
    with open("output.txt",'w') as outfile:
        numcases = int(infile.readline().strip())
        for i in range(1,numcases+1):
            combrules = []
            opprules = []
            invokes = []
            stack = []
            lineelems = infile.readline().split()
            c = int(lineelems[0])
            lineelems = lineelems[1:]            
            if c > 0:
                str1 = ""
                while len(str1) < 3 * c:
                    str1 += lineelems[0]
                    lineelems = lineelems[1:]                       
                for j in range(c):
                    combrules.append(tuple(str1[j*3:j*3+3]))
            d = int(lineelems[0])
            lineelems = lineelems[1:]            
            if d > 0:
                str1 = ""
                while len(str1) < 2 * d:
                    str1 += lineelems[0]
                    lineelems = lineelems[1:]                                       
                for j in range(d):
                    opprules.append(tuple(str1[j*2:j*2+2]))

#            print repr(combrules)
#            print repr(opprules)
            
            n = int(lineelems[0])
            stack = []
            if n > 0:
                for elem in lineelems[1]:
                    stack.append(elem)
                    change = True
                    while change:
                        change = False                    
                        for rule in combrules:
                            for k in range(len(stack)-1):
                                if (stack[k] == rule[0] and stack[k+1]) == rule[1] or (stack[k] == rule[1] and stack[k+1] == rule[0]):
                                    stack[k:k+2] = rule[2]
                                    change = True
                    for rule in opprules:
                        if rule[0] in stack and rule[1] in stack:
                            stack = []
            outfile.write("Case #" + str(i) + ": [" + ", ".join(stack) + "]\n")
