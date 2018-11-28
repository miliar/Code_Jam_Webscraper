
def calculate_case(case_number, finput):

    first_row_number = int(finput.readline())
    for row in xrange(4):
        current_row = finput.readline()
        if (row+1) == first_row_number:
            first_row_values = current_row
    first_row_values = first_row_values.split(" ")
    first_row_values = map(int, first_row_values)

    second_row_number = int(finput.readline())
    for row in xrange(4):
        current_row = finput.readline()
        if (row+1) == second_row_number:
            second_row_values = current_row
    second_row_values = second_row_values.split(" ")
    second_row_values = map(int, second_row_values)


    answer = list(set(first_row_values).intersection(second_row_values))

    if len(answer) == 1:
        message = "Case #" + str(case_number) + ": " + str(answer[0])
    elif len(answer) > 1:
        message = "Case #" + str(case_number) + ": Bad magician!"
    else:
        message = "Case #" + str(case_number) + ": Volunteer cheated!"
    return message

def print_message(message, foutput):
    print message
    foutput.write(message + "\n")

if __name__ == "__main__":
    fin = open('A-small-attempt2.in', 'r')
    fout = open('problema.out','w')
    number_of_cases = int(fin.readline())
    for i in xrange(number_of_cases):
        message = calculate_case(i+1, fin)
        print_message(message, fout)
    fin.close()
    fout.close()



