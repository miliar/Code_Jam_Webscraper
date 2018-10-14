import os

#dealing with reading
folder = os.path.dirname(__file__)
text_files = [f for f in os.listdir(folder) ]
print text_files
filename = u'A-small-attempt0.in'

text_file = open(folder+"/"+filename, "r")

input = []
for line in text_file:  # opened in text-mode; all EOLs are converted to '\n'
    line = line.rstrip('\n')
    input.append(line)    
#print input

#dealing with writing
output = u'A-small-attempt0.out'
out = open(folder+"/"+output,'w')


#specifici problem
tt = int(input[0])
#print tt
op1 = 1
op2 = 6

for x in xrange(tt):
    sh1 = []
    sh2 = []
    hint1 = []
    hint2 = []
    case = x+1
    matches = 0
    result = 0
    
    #print "Case #" + str(x) + ": " 
    choice1 = int(input[op1])
    #print "choice1: ",choice1
    for row in range(1,5):
        sh1.append([int(s) for s in input[op1+row] .split() if s.isdigit()])
    op1 += 10
    #print sh1
    hint1 = sh1[choice1-1]
    #print "hint1:",hint1
    
    choice2 = int( input[op2])
    #print "choice2: ",choice2
    for row in range(1,5):
        sh2.append([int(s) for s in input[op2+row] .split() if s.isdigit()])
    op2 += 10
    #print sh2
    hint2 = sh2[choice2-1]
    #print "hint2:", hint2
    
    for x in range(0,4):
        for y in range(0,4):
            if(hint1[x]==hint2[y]):
                matches += 1
                result = hint1[x]
                
                
    #print "matches:", matches
    if(matches>1):
        out.write("Case #" + str(case) + ": Bad magician!" + "\n")
    if(matches==1):
        out.write( "Case #" + str(case) + ": " + str(result) + "\n")
    if(matches==0):
        out.write("Case #" + str(case) + ": Volunteer cheated!" + "\n")
        
text_file.close()
out.close()