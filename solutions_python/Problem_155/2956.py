f = open('A-Large.in', 'r')
g = open('output_A_Large.txt', 'w')
num_loops = int(f.readline())

for i in range(0,num_loops):
    thisline = f.readline()
    thislinelist = thisline.split()
    num_elements = int(thislinelist[0]) + 1
    #print num_elements
    Slist = thislinelist[1]
    #print Slist

    counter = 0
    difference = 0

    for j in range(0,num_elements):
        needed = j+1
        counter += int(Slist[j])
        if counter < needed:
            difference2 = (needed - counter)
            difference += difference2
            counter += difference2
    #string = str('Case #' + str(i+1) + ': ' + Slist.replace('\n','') + ' , ' + str(difference) + '\n')
    string = str('Case #' + str(i+1) + ': ' + str(difference) + '\n')
    g.write(string)
f.close()
g.close()
