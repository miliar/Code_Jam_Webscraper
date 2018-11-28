from iopart import read_input, write_output

raw_data = read_input(name_of_file = 'B-large.in')
number_of_integers = raw_data[0]
data = raw_data[1]
final_answer = []

def find_tidy(integer):
    string = integer
    length = len(string)
    answer = string
    if answer[0] == '0':
        return find_tidy(answer[1:])
    with_anomaly, position = anomaly_check(string)
    if with_anomaly:
        new_string = string[:position-1] + \
                     str(int(string[position-1]) - 1)+ \
                     '9'*(length-position)         
        answer = find_tidy(new_string)   
    return answer

def anomaly_check(string):
    position = -1
    bool_anomaly = False
    length = len(string)
    if length == 1:
        return(bool_anomaly, position)
    for pos in range(1,length):
        if string[length - pos] < string[length - pos - 1]:
            bool_anomaly = True
            position = length - pos
            break
    return(bool_anomaly, position)

print(data)
for element in data:
    final_answer.append(find_tidy(element))
    
write_output(final_answer, name_of_file = 'B-large.out')