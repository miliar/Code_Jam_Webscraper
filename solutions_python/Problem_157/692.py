class Problem:
    def __init__(self) :
        self.L = 0
        self.X = 0
        self.str = ""

def readProblem(input):
    problem = Problem()
    line = input.readline().rstrip().split()
    problem.L = int(line[0])
    problem.X = int(line[1])
    problem.str = input.readline().rstrip()
    return problem

dijkstra = [ [ "1", "i" , "j", "k"], \
             [ "i" , "-1", "k", "-j"], \
             [ "j", "-k" , "-1", "i"], \
             [ "k", "j" , "-i", "-1"] ]
             
    
lookup = {"1": 0, "i": 1, "j": 2, "k": 3}
    
def compute(a, b) :
    an = 1
    if (a.startswith("-")) : 
        ax = a[1]
        an = -1
    else : 
        ax = a
        
    bn = 1    
    if (b.startswith("-")) : 
        bx = b[1]
        bn = -1
    else : 
        bx = b
    
    value = dijkstra[lookup[ax]][lookup[bx]]
    
    if (an != bn) :
        if (value.startswith("-")) :
            value = value[1]
        else :
            value = "-" + value
    
    return value
     
    
def solveProblem(problem):
    answer = "NO"
    
    concat = ""
    for i in range(problem.X) :
        concat += problem.str
    strlen = len(concat)

    ix = -1
    iv = "1"
    while ((ix + 1 < strlen) and (answer != "YES")) :
        ix += 1
        
        # find a substring that evaluates to "i"
        for i in range(ix, strlen) :
            iv = compute(iv, concat[i])
            if iv == "i" :        
                ix = i
                break

        if iv == "i" :
            jx = ix + 1
            if (jx < strlen) :
                # find a substring that evaluates to j        
                jv = "1"
                for j in range(jx, strlen) :
                    jv = compute(jv, concat[j])
                    if jv == "j" :        
                        jx = j
                        break
                             
                if jv == "j" :                    
                    kx = jx + 1   
                    if (kx < strlen) :
                        kv = "1"
                        for k in range(kx, strlen) :        
                            kv = compute(kv, concat[k])
                        if (kv == "k") :
                            answer = "YES"
        else :
            break
        
    
    return answer



input = open('input.in')
output = open('output.out', 'w')

cases = int(input.readline())
for i in range(cases):
    problem = readProblem(input)
    answer = solveProblem(problem)
	
    output.write("Case #" + str(i+1) + ": " + str(answer) + "\n")

