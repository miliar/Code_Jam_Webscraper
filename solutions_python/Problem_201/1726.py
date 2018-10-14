
f_in = open('C-small-2-attempt2.in', 'r') # C-small-2-attempt1.in

data = f_in.readlines()

f_in.close()

for i in range(len(data)):
    data[i] = data[i][0:len(data[i])-1]

l = []
sol = []

cases = int(data.pop(0))

for i in range(cases):
    entry = data[i].split(' ')
    for i in range(len(entry)):
        entry[i] = int(entry[i])
    l.append(entry)

print('Calculating')

for i in range(len(l)):
    blocks =[l[i][0]]
    occurances = [1]
    customers = l[i][1]
    pos = -1
    y = 0
    z = 0

    for j in range(customers):
        occurances[0] -= 1

        v = blocks[0] - 1

        y = (v // 2) + (v % 2)
        z = v // 2
        
        if y in blocks:
            occurances[blocks.index(y)] += 1
        else:
            blocks.append(y)
            occurances.append(1)

        if z in blocks:
            occurances[blocks.index(z)] += 1
        else:
            blocks.append(z)
            occurances.append(1)
        
        if occurances[0] == 0:
            blocks.pop(0)
            occurances.pop(0)
        
    sol.append('Case #' + str(i+1) + ': ' + str(y) + ' ' + str(z))

f = open('qds2.txt', 'w')
for entry in sol:
    f.write(entry + '\n')
f.close()

print('Done')
