import math

bathroominput = 'C-small-2-attempt0.in'
bathroomoutput = 'C-small-2-attempt0.out'

inputlines = []
with open(bathroominput, 'r') as f:
    inputlines = f.readlines()

numcases = int(inputlines.pop(0))

with open(bathroomoutput,'w') as f:
    for x in range(numcases):
        case = inputlines.pop(0)
        N = int(case.split()[0])
        K = int(case.split()[1])

        remaining = N-K+1
        layer = math.floor(math.log(K)/math.log(2))
        max_space = math.ceil(remaining/(2**layer))
            
        Max = math.ceil((max_space-1)/2)
        Min = math.floor((max_space-1)/2)
        
        strtowrite = 'Case #'+str(x+1)+": "+str(Max)+" "+str(Min)+"\n"
        f.write(strtowrite)


