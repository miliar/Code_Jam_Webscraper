Filename = 'A-small-attempt0.in'

with open(Filename,'r') as file_seq:
    all_lines = list()
    for line in file_seq.readlines():
        line = line.rstrip().split()
        x = list()
        for i in range(len(line)):
            x.append(int(line[i]))
        all_lines.append(x)

numCases = all_lines[0][0]

r = len(all_lines[1:])
i = 1
k = 1
cases = dict()

while i < r:
    first = all_lines[i][0]
    case = list()
    i = i + 1
    for j in range(4):
        case.append(all_lines[i])
        i = i + 1
    first2 = all_lines[i][0]
    case2 = list()
    i = i + 1
    for j in range(4):
        case2.append(all_lines[i])
        i = i + 1
    cases[k] = [first,case],[first2,case2]
    k = k + 1

out = dict()
for i in range(len(cases.keys())):
    case = cases[i+1]
    first_arr = case[0]
    second_arr = case[1]
    l_chose_1 = first_arr[1][first_arr[0]-1]
    l_chose_2 = second_arr[1][second_arr[0]-1]
    x = [l_chose_2[j] for j in range(len(l_chose_2)) if l_chose_2[j] in l_chose_1]
    if len(x) == 1:
         out[i+1] = x[0]
    if len(x) > 1:
         out[i+1] = "Bad magician!"
    if len(x) < 1:
         out[i+1] = "Volunteer cheated!"


filename2 = 'A-small-attempt0.txt'

with open(filename2, 'w') as file_seq:
    for i in range(1,numCases+1):
        s = 'Case #'+str(i)+': '+str(out.get(i))+'\n'
        file_seq.writelines(s)
 
    
