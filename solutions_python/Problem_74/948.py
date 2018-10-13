def calculate_moves(move_list):
    b_time = 0
    o_time = 0
    last_b_position = 1
    last_o_position = 1
    time_taken = 0

    for entry in move_list:
        if 'O' in entry[0]:
            if b_time<=abs(entry[1]-last_o_position):
                o_time = o_time+abs(entry[1]-last_o_position)-b_time+1
                time_taken = time_taken+abs(entry[1]-last_o_position)-b_time+1
            else:
                o_time = o_time+1
                time_taken = time_taken+1
            b_time = 0
            last_o_position=entry[1]
            
        else:
            if o_time<=abs(entry[1]-last_b_position):
                b_time = b_time+abs(entry[1]-last_b_position)-o_time+1
                time_taken = time_taken+abs(entry[1]-last_b_position)-o_time+1
            else:
                b_time = b_time+1
                time_taken = time_taken+1
            o_time = 0
            last_b_position=entry[1]
            
#        print(time_taken,entry[0])
    return time_taken

#file_handle = open('A-small-attempt0.in','r')
#output_file_handle = open('A-small-attempt0.out','w')
file_handle = open('bot_trust_A-large.in','r')
output_file_handle = open('bot_trust_A-large.out','w')

#move_list = [['o',2], ['b',1], ['b',2], ['o',4]]
#move_list = [['o',5], ['o',8], ['b',100]]
#move_list = [['b',2], ['b',1]]

number_of_inputs = file_handle.readline()

case_counter = 0
for line in file_handle:

    move_list = []
    counter = 0
    
    space_seperated_line = line.split(' ')
    number_of_entries = int(space_seperated_line[0])
    space_seperated_line = space_seperated_line[1:]
    
    while counter < number_of_entries:
        move_list.append([space_seperated_line[0],int(space_seperated_line[1])])
        space_seperated_line = space_seperated_line[2:]
        counter = counter+1

    case_counter = case_counter+1
    
#    print('Case #'+str(case_counter)+': '+str(calculate_moves(move_list)))
    output_file_handle.write('Case #'+str(case_counter)+': '+str(calculate_moves(move_list))+'\n')
    
file_handle.close()
output_file_handle.close()

