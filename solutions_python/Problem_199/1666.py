
f_in = open('A-small-attempt0.in', 'r')

data = f_in.readlines()

f_in.close()

for i in range(len(data)):
    data[i] = data[i][0:len(data[i])-1]

l = []
sol = []

cases = int(data.pop(0))

for i in range(cases):
    entry = data[i].split(' ')
    seq = []
    for p in entry[0]:
        if p == '+':
            seq.append(True)
        else:
            seq.append(False)
    entry[0] = tuple(seq)
    entry[1] = int(entry[1])
    
    l.append(entry)

print('Calculating')

for i in range(len(l)):
    visited = []
    target = tuple([True for j in range(len(l[i][0]))])
    queue = [(target, 0)]
    spat = l[i][1]

    found = False
    while len(queue) != 0:
        at = queue.pop(0)
        if (at[0] in visited) == False:
            visited.append(at[0])
            if at[0] == l[i][0]:
                found = True
                sol.append('Case #' + str(i+1) + ': ' + str(at[1]))
                break

            for j in range(len(at[0]) - spat + 1):
                queue.append((at[0][0:j] + tuple([not at[0][j + k] for k in range(spat)]) + at[0][j+spat:len(at[0])], at[1] + 1))
            
    
    if found == False:
        sol.append('Case #' + str(i+1) + ': IMPOSSIBLE')

f = open('pAnc4K3s.txt', 'w')
for entry in sol:
    f.write(entry + '\n')
f.close()

print('Done')
