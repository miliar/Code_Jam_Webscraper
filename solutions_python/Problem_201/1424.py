import numpy as np

def closed_form(stall_count, person_count):
    
    if stall_count == person_count:
        return 0, 0
    
    depth = np.floor(np.log(person_count) / np.log(2)) - 1
    divisions = np.floor((stall_count - (2 ** (depth + 1) - 1)) / 2 ** (depth + 1))
    remainder = np.remainder(np.floor(stall_count - (2 ** (depth + 1) - 1)), 2 ** (depth + 1))
    last_position = person_count - (2 ** (depth + 1) - 1)
    
    branch_index = remainder - last_position
    if branch_index >= 0:
        branch = divisions + 1
    else:
        branch = divisions
        
    if branch % 2 == 0:
        maximum = np.floor((branch - 1) / 2) + 1
        minimum = np.floor((branch - 1) / 2)
    else:
        maximum = np.floor(branch / 2)
        minimum = maximum
        
    return int(maximum), int(minimum)

with open('problemC.txt', 'r') as file:
    array = []
    for line in file:
        if line != '':
            array.append(line.replace('\n',''))
    array = array[1:]
    print(array)
 
with open('problemC2soln.txt','w',encoding='utf-8') as file:
    file.write('')
    for t,case in enumerate(array):
        res = closed_form(int(case.split(' ')[0]),int(case.split(' ')[1]))
        file.write('Case #'+str(t+1)+': ' + str(res[0]) + ' ' + str(res[1]) + '\n')