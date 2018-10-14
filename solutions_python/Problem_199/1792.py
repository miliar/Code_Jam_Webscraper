def isNotHappy(cakes):
    for cake in cakes:
        if cake == '-':
            return True
    return False

def flip(cake):
    if cake == '-':
        return '+'
    else:
        return '-'

    
def flipPancakes(cakes, S):
    flips = 0
    while isNotHappy(cakes):
        counter = 0 #index of '-'
        cakes = list(cakes)
        
        
        #iterate from left to right
        for cake in cakes:
            if cake == '-': #if there is '-', flip
                #check if can flip
                if counter + S > len(cakes): #cannot flip
                    return "IMPOSSIBLE"
                else: #flip
                    for i in range(counter,counter+S):
                        cakes[i] = flip(cakes[i])
                    flips += 1
            counter += 1

    return flips
        
        
filename = "A-large.in"
infile = open(filename, 'r')
lines = infile.readlines()

cases = []
t = int(lines[0].strip('\n'))
for i in range(1,t+1):
    cases.append(lines[i].strip('\n').split(' ')) #e.g. ["-+---+", 4]
infile.close()

outfile = open("A-large.out", 'w')

caseNo = 1
for case in cases:
    result = flipPancakes(case[0],int(case[1]))
    outfile.write("Case #{}: {}\n".format(caseNo, result))
    caseNo += 1

outfile.close()
