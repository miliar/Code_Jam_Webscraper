f_in = open('A-large.in', 'r')

data = f_in.readlines()

f_in.close()

for i in range(len(data)):
    if data[i][-1] == '\n':
        data[i] = data[i][0:len(data[i])-1]

l = []
sol = []

cases = int(data.pop(0))

in_case = 0
case = [0,[]]

case_data = []

for line in data:
    entry = line.split(' ')
    seq = []
    for num in entry:
        seq.append(int(num))
    if in_case == 0:
        case[0] = seq[0]
        in_case = seq[1]
    else:
        in_case -= 1
        case[1].append(seq)
        if in_case == 0:
            case_data.append(case)
            case = [0, []]

sol = []

print(case_data)

case_on = 1
for case in case_data:
    kilometers = case[0]
    horses = case[1]
    speed = 0.0
    
    for horse in horses:
        horse.append((kilometers-horse[0])/horse[1])
        
    for i in range(len(horses)):
        horses[i] = tuple(horses[i])
    
    horses = sorted(horses)
    
    actual = [horses[0]]
    
    for horse in horses[1:]:
        if horse[2] > actual[-1][2]:
            actual.append(horse)
            
    fastest = actual[0][2]
    
    for horse in actual[1:]:
        if horse[2] > fastest:
            fastest = horse[2]

    sol.append('Case #' + str(case_on) + ': ' + '{0:.6f}'.format(kilometers/fastest))
    case_on += 1

f = open('cc_large.txt', 'w')
for entry in sol:
    f.write(entry + '\n')
f.close()

print('Done')
    
