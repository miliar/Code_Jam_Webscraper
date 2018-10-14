

def read_file(file_name):
    f = open(file_name, 'r')
    first_line = f.readline()
    return_str = ""
    for i in range(0, int(first_line)):
        number = int(f.readline())
        return_str += 'Case #'+str(i+1)+': '+str(get_tidy_number(number))
        return_str += '\n'

    return return_str

def is_tidy_number(number):
        if number < 10:
            return True
        str_number = str(number)
        for i in range(0, len(str_number) - 1):
            if not (int(str_number[i]) <= int(str_number[i + 1])):
                return False

        return True



def get_tidy_number(number):
    iteration = 1
    while(not is_tidy_number(number)):
        number = (number - (number%(10**iteration) + 1))
        iteration = iteration + 1
    return number

output = read_file('B-large.in')
output_file = open('output.txt', 'w')
output_file.write(output)
output_file.close()