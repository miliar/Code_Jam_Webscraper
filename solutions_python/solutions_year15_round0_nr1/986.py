

# levels is string of how many people has each shyness level, bad name
def getMinPeople(s,levels):
    people = 0
    additional = 0
    for i in range(s+1):
        amount_of_people = int(levels[i])
        if amount_of_people > 0:          
            if people < i:
                extra = i - people
                additional += extra
                people += extra
            people += amount_of_people
    return additional

f = open("one.in", "r").read()

#new_file = open("sma.txt", "w")
splitted_file = f.split("\n")[:]

lineCounter =1
amountOfLines = len(splitted_file)

case = 0

while(lineCounter < amountOfLines-1):
    case += 1
    firstLine = splitted_file[lineCounter]
    lineCounter += 1
    s = int(firstLine.split(" ")[0])
    levels = firstLine.split(" ")[1]
    out = getMinPeople(s,levels)
    print "Case "+ "#"+str(case) +": " + str(out)
    
    
