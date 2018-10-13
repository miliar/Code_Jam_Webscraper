special_cases = 0
input_file = open('input.in', 'r')
output_file = open('output.txt', 'w')

def test_contest(contest_data):
    global special_cases
    
    contest_data_list = contest_data.split(' ')
    contestants = int(contest_data_list[0])
    special_cases = int(contest_data_list[1])
    highest_score = int(contest_data_list[2])
    high_score_contestants = 0
    
    for contestant in contest_data_list[3:]:
        high_score_contestants += test_contestant(int(contestant), highest_score) 

    return high_score_contestants
    
def test_contestant(total_score, highest_score):
    global special_cases
    dividend = total_score / 3
    reminder = total_score % 3
    
    if(total_score == 0 and highest_score != 0):
        return 0;
    
    if(dividend >= highest_score or (reminder != 0 and (dividend + 1) >= highest_score)):
        return 1
    
    if(special_cases != 0):
        if((reminder == 0 and (dividend+1) >= highest_score) or 
           (reminder != 0 and (dividend + reminder) >= highest_score)):
            special_cases-=1
            return 1
      
    return 0
    
lines = input_file.readlines()
input_file.close()

cases = int(lines[0])

for case in range(cases):
    case_result = test_contest(lines[case+1])
    output_file.write("Case #" + str(case+1) + ": " + str(case_result) + "\n")

output_file.close()