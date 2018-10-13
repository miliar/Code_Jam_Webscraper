input_file = open('A-small-attempt0.in','r')
raw_input = input_file.read()

lines = raw_input.split('\n')

num_cases = int(lines[0])
case_num = 1

output_text = ''
output_file = open('1.out','w')
output_text = ''
start_line = 0

debug=0

while case_num<=num_cases:
    start_line = 1 + (case_num-1)*10
    
    row1 = int(lines[start_line])
    row2 = int(lines[start_line+5])
    #print(row1)
    #print(row2)

    possible1 = lines[start_line+row1].split(' ')
    possible2 = lines[start_line+5+row2].split(' ')
    answer = [card for card in possible2 if card in possible1]

    if debug:
        print(possible1)
        print(possible2)
        print(answer)
        print('\n')

    if len(answer)==0:
        output_text += 'Case #'+str(case_num)+': Volunteer cheated!\n'
    elif len(answer)==1:
        output_text += 'Case #'+str(case_num)+': '+str(answer[0])+'\n'
    elif len(answer)>1:
        output_text += 'Case #'+str(case_num)+': Bad magician!\n'
    else:
        print('ERROR - answer list is not a length??')

    if debug: print(output_text)
    
    case_num += 1

output_file.write(output_text)
input_file.close()
output_file.close()
