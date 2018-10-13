input_file = open("input.in", 'r')
output_file = open("output.out", 'w')

def file_input():
    input_string = input_file.readline()
    if input_string[-1] == '\n':
        input_string = input_string[:-1]
    return input_string

def tidy_check(listy):
    for i in range(len(listy) - 1):
        if listy[i] > listy[i+1]:
            return False
    return True

def tidy_print(listy):
    string = ''
    for i in listy:
        string += str(i)
    while string[0] == '0':
        string = string[1:]
    return string

def formatted(x, listy):
    s = tidy_print(listy)
    return "Case #" + str(x) + ': ' + s + '\n'

testcases = int(file_input())

for x in range(1, testcases + 1):
    listy = []
    for i in file_input():
        listy.append(int(i))

    length = len(listy)
    i = 0
    while i < length - 1:
        if listy[i] > listy[i+1]:
            listy[i] -= 1
            for j in range(i+1, length):
                listy[j] = 9
            length = i + 1
            i = -1
        i += 1

    output_file.write(formatted(x, listy))
    
input_file.close()
output_file.close()
