'''
Created on Apr 12, 2014

@author: Federico
'''
lst_number = [line.strip() for line in open('A-small-attempt0.in', "r")][::-1]
file_solution = open('result.txt', 'w')
number_test = int(lst_number.pop())

for i in range(number_test):
    answer1 = int(lst_number.pop())
    for j in range(1, 5):
        if j == answer1:
            row1 = lst_number.pop().strip().split()
        else:
            lst_number.pop()
    answer2 = int(lst_number.pop())
    for j in range(1, 5):
        if j == answer2:
            row2 = lst_number.pop().strip().split()
        else:
            lst_number.pop()
    
    result = list(set(row2) & set(row1))
    
    if len(result) == 1:
        file_solution.write("Case #{}: {}\n".format(i+1, result[0]))
    elif len(result) > 1:
        file_solution.write("Case #{}: Bad magician!\n".format(i+1))
    elif len(result) == 0:
        file_solution.write("Case #{}: Volunteer cheated!\n".format(i+1))

file_solution.close()