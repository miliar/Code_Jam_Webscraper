input_file = open("input.in", 'r')
output_file = open("output.out", 'w')

colors = ['R', 'O', 'Y', 'G', 'B', 'V']

def file_input():
    input_string = input_file.readline()
    if input_string[-1] == '\n':
        input_string = input_string[:-1]
    return input_string

def formatted(x, y):
    return "Case #" + str(x) + ': ' + str(y) + '\n'

def max_index(listy):
    maxy = 0
    index = 0
    for i in range(6):
        if listy[i] > maxy:
            maxy = listy[i]
            index = i
    return index

testcases = int(file_input())

for x in range(1, testcases + 1):
    listy = [int(i) for i in file_input().split()]
    n = listy.pop(0)

    answer = [''] * n

    index = max_index(listy)

    if listy[index] > n/2:
        y = "IMPOSSIBLE"
        #print n, listy, y
        output_file.write(formatted(x, y))
        continue


    temp = (n+1) / 2
    marked = 0

    while temp:
        index = max_index(listy)
        if listy[index] < temp:
            for i in range(listy[index]):
                answer[2*(marked + i)] = colors[index]
            marked += listy[index]
            temp -= listy[index]
            listy[index] = 0
        else:
            for i in range(temp):
                answer[2*(marked + i)] = colors[index]
            for i in range(listy[index] - temp):
                answer[2*i + 1] = colors[index]
            marked = listy[index] - temp
            listy[index] = 0
            break

    for i in range(6):
        for j in range(listy[i]):
            answer[2*(marked + j) + 1] = colors[i]
        marked += listy[i]
        
            
    #print n, listy, answer

    y = ''

    for i in answer:
        y += i
    
    output_file.write(formatted(x, y))
    
input_file.close()
output_file.close()
