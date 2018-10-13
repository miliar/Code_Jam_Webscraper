f = open('part1.txt')
lines = f.readlines()
f.close()
    
output = open('Output.txt','w')
counter = 0
i = 0
while(i != int(lines[0])):
    first_answer = lines[i*10 + 1]
    second_answer = lines[i*10+6]    
    first_line = (lines[int(first_answer) + i*10 + 1]).split()
    second_line = (lines[int(second_answer) + i*10 + 6]).split()
    for n1 in first_line:
        for n2 in second_line:
            if n1 == n2:
                counter += 1
                number = n1
                
    if counter == 1:      
        output.write("Case #" + str(i+1) + ": " + str(number) + "\n")
    elif counter > 1:
        output.write("Case #" + str(i+1) + ": " + "Bad Magician!\n")
    elif counter == 0:
        output.write("Case #" + str(i+1) + ": " + "Volunteer Cheated!\n")
    i += 1
    counter = 0
output.close() 