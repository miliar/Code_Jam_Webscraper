def scanf(array, line, *args):
    yield line+1
    toks = [array[line].replace('\n', '')]
    for i in range(len(args)):
        yield args[i](toks[i])
        
        
f = open("A2.in", "r")
line = 0
dat = f.readlines()
f.close()

line, n = scanf(dat, line, int)

f = open("A2.out", "w")

for i in range(n):

    line, s = scanf(dat, line, int)
    
    engines = []
    states  = []
    used = 0
    switches = 0
    
    for j in range(s):
        line, name = scanf(dat, line, str)
        engines.append(name)
        states.append(False)

    #print engines
    #print states
    
    line, q = scanf(dat, line, int)
    for j in range(q):
        line, name = scanf(dat, line, str)
        k = engines.index(name)

        if not states[k]:
            states[k] = True
            used += 1

        if used == s:
            switches += 1
            for l in range(s):
                states[l] = False
            states[k] = True
            used = 1

        #print name, k
        #print states
        #print used
        #print switches
        

    f.write("Case #%d: %d\n"%(i+1, switches))
f.close()

            
        

        
    


    

    
