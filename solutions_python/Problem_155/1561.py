input_file = open("A-large.in")
output_file = open("standing_ovation.txt", "w")
Testcases = int(input_file.readline()[:-1])


def calc_shyness(string):
    '''
    To seperate the 2 parts of a line and return as a list
    '''
    for letter in range(len(string)):
        if string[letter] == ' ':
            return [int(string[:letter]), string[letter+1:]]

def calc_friends(string):
    '''
    calculates the least number of friends required
    '''
    temp_list = calc_shyness(string)
    friends = 0
    audience = 0
    for shyness in range(temp_list[0] + 1):
        if shyness > audience and temp_list[1][shyness] != '0':
            friends += shyness - audience
            audience += shyness - audience
        audience += int(temp_list[1][shyness])
    return str(friends)

#main body of the program
for test in range(Testcases):
    current_case = input_file.readline()
    if current_case[-1] == '\n':
        current_case = current_case[:-1]
    output_string = "Case #" + str(test + 1) + ": " + calc_friends(current_case) + '\n'
    output_file.write(output_string)


input_file.close()
output_file.close()
