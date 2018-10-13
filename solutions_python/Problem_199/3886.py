def NotHappy(cakes):
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
    while NotHappy(cakes):
        count = 0 #index of '-'
        cakes = list(cakes) #e.g. "++--++" --> [+,+,-,-,+,+]
        
        #iterate from left to right
        for cake in cakes:
            if cake == '-': #if there is '-', flip
                #check if can flip
                if count + S > len(cakes): #cannot flip
                    return "IMPOSSIBLE"
                else: #flip
                    for i in range(count,count+S):
                        cakes[i] = flip(cakes[i])
                    flips += 1
            count += 1

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
