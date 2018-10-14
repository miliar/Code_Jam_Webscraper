input_file = open("input.in", 'r')
output_file = open("output.out", 'w')

def file_input():
    input_string = input_file.readline()
    if input_string[-1] == '\n':
        input_string = input_string[:-1]
    return input_string.split()

def formatted(x, y):
    return "Case #" + str(x) + ': ' + str(y) + '\n'

testcases = int(file_input()[0])

for x in range(1, testcases + 1):
    n, k = file_input()
    n = int(n)
    k = int(k)

    listy = [n]
    #print n, k
    for i in range(k - 1):
        listy.sort(reverse = True)
        z = listy.pop(0)
        listy.append(z/2)
        if z % 2 == 0:
            listy.append(z/2 -1)
        else:
            listy.append(z/2)
        while listy[-1] == 0:
            listy.pop()

    #print listy
    listy.sort(reverse = True)
    z = listy.pop(0)
    string = str(z/2) + ' '
    if z % 2 == 0:
        string += str(z/2 -1)
    else:
        string += str(z/2)
    
    output_file.write(formatted(x, string))
    
input_file.close()
output_file.close()
