def delim(line):
    items = []
    item = ''
    for c in line:
        if c != ' ':
            item += c
        else:
            items.append(item)
            item = ''
    items.append(item[:-1])
    return items

def strListToInt(items):

    for i in range(len(items)):
        items[i] = int(items[i])
    return items
    

def solve(row1,row2):
    matches = 0
    for c in row1:
        if c in row2:
            card = c
            matches += 1
    if matches == 1:
        return str(card)
    elif matches > 1:
        return "Bad magician!"
    else: return "Volunteer cheated!"



    
    

 


f = open("A-small-attempt0.in",'r')
outf = open('magic.txt','w')

lines = f.readlines()
T = int(lines[0]) #number of cases
caseIndex = 0;
for i in range(T):
    n1 = int(lines[caseIndex+1])
    row1 = strListToInt(delim(lines[caseIndex+1+n1]))
    n2 = int(lines[caseIndex+6])
    row2 = strListToInt(delim(lines[caseIndex+6+n2]))
    
    

    caseIndex += 10
    outf.write("Case #" + str(i+1) + ": " + solve(row1,row2) + "\n")
    

outf.close()
