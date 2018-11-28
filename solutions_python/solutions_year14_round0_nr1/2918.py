file = open('A-small-attempt8.in.txt', 'r')
file = file.readlines()
number_of_test_cases = int(file[0])
counter = 1
output = open('output.text', 'a')
foo = ""
bar = 1
for line in range(1, len(file), 10):
    vol_input_1 = int(file[line]) + line
    vol_input_2 = int(file[line + 5]) + line + 5
    row = []
    row_2 = []
    one, two, three, four = file[vol_input_1].split()
    row.append(one)
    row.append(two)
    row.append(three)
    row.append(four)
    one, two, three, four = file[vol_input_2].split()
    row_2.append(one)
    row_2.append(two)
    row_2.append(three)
    row_2.append(four)
    counter = []
    for item in row:
        for item_2 in row_2:
            if item == item_2:
                counter.append(item)
##    print(file[vol_input_1])
##    print(file[vol_input_2])
##    print(len(counter))
    if len(counter) == 1:
        foo += 'Case #{0}: {1}\n'.format(bar, counter[0])
    elif len(counter) == 0:
        foo += 'Case #{0}: Volunteer cheated!\n'.format(bar)
    else:
        foo += 'Case #{0}: Bad magician!\n'.format(bar)
    bar += 1 
output.write(foo) 
output.close()
                     
    



            
        
    
