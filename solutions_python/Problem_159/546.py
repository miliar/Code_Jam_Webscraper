input_file = open("mush2.IN")
output_file = open("mushroom_fever.txt", 'w')
Testcases = int(input_file.readline()[:-1])

def mushroom_seperate(string):
    '''
    seperate the musroom count on the plate
    '''
    if string[-1] != ' ':
        string += ' '
    start = 0
    listy = []
    length = len(string)
    for index in range(length):
        if string[index] == ' ':
            listy.append(int(string[start:index]))
            start = index + 1
    return listy

def method1(listy, n):
    count = 0
    for i in range(n - 1):
        if listy[i] > listy[i+1]:
            count += listy[i] - listy[i + 1]
    return str(count)
    

def method2(listy, n):
    miny = 0
    for i in range(n - 1):
        if listy[i] - listy[i+1] > miny:
            miny = listy[i] - listy[i + 1]
    count = 0
    for i in range(n - 1):
        if listy[i] >= miny:
            count += miny
        else:
            count += listy[i]
    return str(count)
        

#main body of the program 
for test in range(Testcases):
    current_case = int(input_file.readline()[:-1])
    current_mushrooms = input_file.readline()
    if current_mushrooms[-1] == '\n':
        current_mushrooms = current_mushrooms[:-1]
    current_mushrooms_list = mushroom_seperate(current_mushrooms)
    output_string = "Case #" + str(test + 1) + ": " + method1(current_mushrooms_list, current_case) + ' ' + method2(current_mushrooms_list, current_case) + '\n'
    output_file.write(output_string)

input_file.close()
output_file.close()

