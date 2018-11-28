#open the file with given input


def get_row(r):
    pass

def compare_rows(row1, row2):
    pos_nums = []
    #check each element in first row if it is in second
    for num in row1:
        if num in row2:
            pos_nums.append(num)
    
    if len(pos_nums) == 1:
        #the card was guessed
        return str(pos_nums[0])
    elif len(pos_nums) == 0:
        #ambigous anwser
        return 'Volunteer cheated!'
    #card wasn't guessed
    return 'Bad magician!'


if __name__ == '__main__':


    test = open('A-small-attempt3.in', 'rb')
    results = []

    lines = test.readlines()
    
    #walk trough whloe file
    cases = int(lines[0])
     
    
    #first two outside the main loop
    first_row = lines[1 + int(lines[1])].strip().split(' ')
    second_row = lines[1+ int(lines[6])].strip().split(' ')
    result.append(compare_rows(first_row, second_row))
    
    for i in range(1,len(lines),10):
        #get current case:
        #first line is the first row
        row1_index = int(lines[i])
        row2_index = int(lines[i + 5])+ 5
        first_row = lines[i+ row1_index].rstrip().split(' ')
        second_row = lines[i + row2_index].rstrip().split(' ')
        results.append(compare_rows(first_row, second_row))
        print 'first row: ', first_row
        print 'second row:', second_row
        
        
        
        
    output = open('output.in', 'wb')
    
    #print out the output

    
    for i in range(cases):
        print a
        a = 'Case #' + str(i+1) + ': ' + results[i] 
        output.write(a + '\n')
    output.close()
