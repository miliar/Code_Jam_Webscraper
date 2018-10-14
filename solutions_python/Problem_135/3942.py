# Opens the input file provided by codejam problem, 
# The file is referenced using full path name, this should be changed for running on different compters
input_file = open(r'/home/gupta/codejam/qa/A-small-attempt4.in','r')

# the first line of input file contains number of cases i.e. line 0
# this input will be grouped in "10 lined inputs" for each test case 
# each card arrangement is from line 2 to 5
# second card arrangement is from line 7 to 10
# the row number chosen by volunteer for first card arrangement will be in line 1
# the row number chosen by volunteer for second card arrangement will be in line 6

# write the result of program in it as per the format specified
output_file = open(r'/home/gupta/codejam/qa/A-small-attempt4.out','w')

# used to save the first arrangement of cards
matrix_first = []

# used to save the second arrangement of cards
matrix_second = []

# used to store the row chosen for 1st arrangement
row_chosen_first = None

# used to store the row chosen for 2nd arrangement
row_chosen_second = None

# used to keep track of line of input
# each case's input contains 10 lines
# this counter is used to keep track 
#and get the required strings out of input
line_counter = 0

# keeps track of case number
case_num = 0
case_total = 0
# Reads line of the input file line by line and store the string in line variable
for line in input_file:
    # Strip the line of trailing or preceding white spaces
    stripped_line = line.strip()
    if line_counter ==0:
        case_total = int(stripped_line)
    # execute if the line postition is between 1 and 10 that is the line currently being read
    if line_counter > 0 and line_counter <= 10:
        # if the line number of the current case is between 2 and 5
        if line_counter >= 2 and line_counter <=5:
            # get the first card arrangement from input and store it in form of a 2d list
            matrix_first.append(stripped_line.split(" ")) 
            # .split() function creates a list of number from the string stored in line variable 
        elif line_counter >= 7 and line_counter <= 10:
            # get the second card arrangement from input and store it in form of a 2d list
            matrix_second.append(stripped_line.split(" "))
        elif line_counter == 1:
            # get the row chosen for first arrangement
            # stored in int so as will be used to access the row numbers using it
            row_chosen_first = int(stripped_line)
        elif line_counter == 6:
            # get the row chosen for second arrangement
            # stored in int so as will be used to access the row numbers using it
            row_chosen_second = int(stripped_line)
    
    # update the line counter which is used to keep the track of line number
    if line_counter < 10 and len(stripped_line)>0:
        line_counter = line_counter + 1
        
    # when the line 10 is reached of each test case input, the counter is reset to one
    # and procesing is done for the current test case
    elif line_counter == 10 :
        # update the case num
        case_num = case_num + 1
        #update the line counter
        line_counter = 1
        # used to store the matching cards from rows chosen in both the arrangement 
        matching_cards = []
        # iterate over each number of row chosen for 1st arrangement
        for i in matrix_first[row_chosen_first-1]:
            # iterate over each number of row chosen for 2nd arrangement
            for j in matrix_second[row_chosen_second-1]:
                # if the numbers of card matches then save them in matching card list
                if int(i) == int(j):
                    matching_cards.append(int(j))
        # produce the output according the required criterion
        # if only one match is found the magic tricked worked and return the number
        if len(matching_cards) == 1:
            output_file.write("Case #"+str(case_num)+": "+str(matching_cards[0]))
        # if no match is found the volunteered lied return the appropriate msg
        elif len(matching_cards) == 0:
            output_file.write("Case #"+str(case_num)+": Volunteer cheated!")
        # if more one match is found the magic tricked didn;t worked and return appropriate msg
        elif len(matching_cards) > 1:
            output_file.write("Case #"+str(case_num)+": Bad magician!")
        if case_num != case_total:
            output_file.write('\n')
            
        # reset and empty the list for later cases
        matrix_first = []
        matrix_second = []
        matching_cards = []
        
# close the files at end
if(not input_file.closed):
    input_file.close()  
if(not output_file.closed):
    output_file.close()   