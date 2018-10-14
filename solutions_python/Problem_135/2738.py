def listify(string):
    
    an = []
    string = string.split()
    for i in string:
        an.append(int(i))
    return an

testfile = open("test.txt")
outputFile = open("output.txt", "w")

noCases = int(testfile.readline().strip())
for i in range(noCases):
    a = int(testfile.readline()) - 1
    first = []
    for j in range(4):
        first.append(listify(testfile.readline()))
    b = int(testfile.readline()) - 1
    second = []
    for j in range(4):
            second.append(listify(testfile.readline()))    
    k = set(first[a]).intersection(set(second[b]))
    
    if len(k) == 1:
        outputFile.write("Case #" + str(i + 1) + ": " + str(k.pop()))
        outputFile.write('\n')
    elif len(k) ==0:
        outputFile.write("Case #" + str(i +1) + ": Volunteer cheated!")
        outputFile.write('\n')
    else:
        outputFile.write("Case #" + str(i+1) + ": Bad magician!")
        outputFile.write('\n')
        
outputFile.close()
    
