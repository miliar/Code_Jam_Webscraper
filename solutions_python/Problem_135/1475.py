fin = open("A-small-attempt0.in", "r")
fout = open("output.txt","w")
s = int(fin.readline()[:-1])
i = 0

while i < s :
    table1 = []
    table2 = []
    row1 = 0
    row2 = 0
    row1 = int(fin.readline()[:-1])
    #print(row1)
    
    for x in range(4):
        line = fin.readline()
        if row1 == x+1 :
            table1.append(line[:-1].split())
    #print(table1)
    row2 = int(fin.readline()[:-1])
    #print (row2)
    
    for y in range(4):
        line = fin.readline()
        if row2 == y+1 :
            if '\n' in line :
                table2.append(line[:-1].split())
            else:
                table2.append(line.split())
    #print(table2)
    i += 1
    
    element = []
    counter = 0
    for z in range(4):
        if table1[0][z] in table2[0] :
            counter += 1
            element.append(table1[0][z])
    #print(element)
    #print(counter)
    if counter == 1 :
        fout.write("Case #" + str(i) +": " + str(element[0]) + '\n')
    elif counter > 1 :
        fout.write("Case #" + str(i) +": " + "Bad magician!" + '\n')
    elif counter == 0 :
        fout.write("Case #" + str(i) +": " + "Volunteer cheated!" + '\n')
fout.close()
    
      
