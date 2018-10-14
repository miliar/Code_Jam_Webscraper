f = open("shynessInput.txt", "r")
string = f.read()
words = string.split()

print(words)
caseNo = 0
for y in range (1,int(words[0])*2,2):
    length = words[y]
    people = words[y+1]
    ##print(people, end="->")
    caseNo += 1
    
    count = 0
    friends = 0
    counter= 0
    for x in people:
        count = count + int(x)
        counter+=1
        ##print(count, "->",counter, end=" ")
        if(count < counter):
            friends = friends + 1
            count = count+1
    print("Case #", caseNo, ": ", friends, sep="")    