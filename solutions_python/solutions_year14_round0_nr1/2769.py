# Google Jam code - Yuval Feinstein

  
def game(T):
    output_file = open('output.txt','w')
    with open(T) as input_file:
        test_ammount = int(input_file.readline())
        for test_case in range(test_ammount):
            # Let's get the relevant line from the first matrice
            first_line_num = int(input_file.readline())
            for non_relevant_line in range(first_line_num - 1):
                input_file.readline()
            first_line = [x for x in input_file.readline().replace('\n','').split(' ')]
            for non_relevant_line in range(4 - first_line_num):
                input_file.readline()
            # Let's get the relevent line from the second matrice
            second_line_num = int(input_file.readline())
            for non_relevant_line in range(second_line_num - 1):
                input_file.readline()
            second_line = [x for x in input_file.readline().replace('\n','').split(' ')]
            for non_relevant_line in range(4 - second_line_num):
                input_file.readline()

            # Let's see FIRST_MAT_LINE and SECOND_MAT_LINE intersection:
            # * if this is empty the user cheated
            # * if there is one value - this is the value
            # * if there is more than one value - the magican cheated
            intersection = [x for x in first_line if x in second_line]
            if len(intersection) == 0:
                output_file.write('case #' + str(test_case + 1) +': Volunteer cheated!\n')
            elif len(intersection) == 1:
                output_file.write('case #' + str(test_case + 1) + ': ' + intersection[0] + '\n')
            else:
                output_file.write('case #' + str(test_case + 1) + ': Bad magician!\n')
    output_file.close()

            
                
                
        
            
        

