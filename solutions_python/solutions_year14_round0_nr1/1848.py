open('output.in','w').close()

def CommonElement(list1,list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

with open('input.in') as file:
    lines = file.readlines()
    line = 0
    T = int(lines[line])
    line += 1
    for i in range(T):
        answer1 = int(lines[line])
        row1 = lines[line+answer1].split()
        line += 5
        answer2 = int(lines[line])
        row2 = lines[line+answer2].split()
        chosen_cards = CommonElement(row1,row2)
        if len(chosen_cards) == 1:
            with open('output.in','rw+') as file:
                file.seek(0, 2)
                file.write('Case #'+str(i+1)+': '+str(chosen_cards[0])+'\n')
        elif len(chosen_cards) == 0:
            with open('output.in','rw+') as file:
                file.seek(0, 2)
                file.write('Case #'+str(i+1)+': Volunteer cheated!\n')
        elif len(chosen_cards) > 1:
            with open('output.in','rw+') as file:
                file.seek(0, 2)
                file.write('Case #'+str(i+1)+': Bad magician!\n')
        line += 5
