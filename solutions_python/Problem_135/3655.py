f = open('a.small.in')
lines = f.readlines()
cases = int(lines[0])
f.close();

f_out = open('a.small.out', 'w');

curr_line = 1
for i in range(cases):
    answer1 = int(lines[curr_line])
    answer2 = int(lines[curr_line + 5])
    arrangement1 = []
    arrangement2 = []
    
    for j in range(4):
        curr_line += 1
        arrangement1.append(lines[curr_line].strip().split(' '))
        
        
    curr_line += 1
    for j in range(4):
        curr_line += 1
        arrangement2.append(lines[curr_line].strip().split(' '))
        
    match = []
    for card in arrangement1[answer1-1]:
        if card in arrangement2[answer2-1]:
            match.append(card)
            
    if len(match) == 0:
        #Volunteer Cheated!
        f_out.write("Case #" + str(i+1) + ": Volunteer cheated!\n")
    elif len(match) == 1:
        #Output card
        f_out.write("Case #" + str(i+1) + ": " + str(match[0]) + "\n")
    else: #match > 1
        #Bad Magician!
        f_out.write("Case #" + str(i+1) + ": Bad magician!\n")
        
    curr_line += 1
        
f_out.close();