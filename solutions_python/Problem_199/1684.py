input_file = open("input.in", 'r')
output_file = open("output.out", 'w')

def file_input():
    input_string = input_file.readline()
    if input_string[-1] == '\n':
        input_string = input_string[:-1]
    return input_string.split()

def formatted(x, y):
    return "Case #" + str(x) + ': ' + str(y) + '\n'

def change(string, i):
    if string[i] == '+':
        string = string[:i] + '-' + string[i+1:]
    else:
        string = string[:i] + '+' + string[i+1:]
    return string

testcases = int(file_input()[0])

for x in range(1, testcases + 1):
    string, flips = file_input()
    length = len(string)
    flips = int(flips)
    count = 0
    for i in range(length - flips + 1):
        if string[i] == '-':
            for j in range(flips):
                string = change(string, i+j)
            count += 1
    for i in range(flips):
        if string[length - i - 1] == '-':
            count = "IMPOSSIBLE"
            break
    output_file.write(formatted(x, count))
    
input_file.close()
output_file.close()
