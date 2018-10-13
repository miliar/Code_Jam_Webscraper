infile = open("A-large.in.txt")
outfile = open("codejamoutput.txt",'w')

firstline = infile.readline().split(" ")
L = int(firstline[0])
D = int(firstline[1])
N = int(firstline[2])

dictionary = []
posswords = []

for x in range(D):
    e = ""
    k = infile.readline()
    for a in k:
        if a!="\n":
            e = e + a
    dictionary.append(e)

inside = False
for y in range(N):
    inside = False
    posswords = []
    line = infile.readline()
    for i in range(len(line)):
        if line[i]=="\n":
            continue
        if line[i]=="(":
            inside = True
            w = ""
            continue
        if inside:
            if line[i]!=")":
                w = w + line[i]
            else:
                posswords.append(w)
                inside = False
        else:
            posswords.append(line[i])
 
    count = 0
    
    for word in dictionary:
        isthere = True
        for d in range(L):
            if word[d] not in posswords[d]:
                isthere = False
        if isthere:
            count = count + 1
            
    
    
  
          
    
    outfile.write("Case #"+str((y+1))+": ")   
    outfile.write(str(count))
    outfile.write("\n")
    
    
        