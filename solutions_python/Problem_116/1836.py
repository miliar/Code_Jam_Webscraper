file = open('A-large.in', 'r')

data = file.read()

file.close()

data = data.strip('\n')
data = data.split('\n')

numCases = data[0]

data.pop(0)

result = ''
index = 1

print(len(data))
for i in range(0, len(data), 5):
    found = False
    grid = data[i]+data[i+1]+data[i+2]+data[i+3]
    print(grid)
    for d in range(i, i+4):
        if data[d].count('X') + data[d].count('T') == 4:
            result += 'Case #'+str(index)+': X won'
            found = True
            break
        if data[d].count('O') + data[d].count('T') == 4:
            result += 'Case #'+str(index)+': O won'
            found = True
            break
        
    if found == False:
        for d in range(0, 4):
            col = data[i][d]+data[i+1][d]+data[i+2][d]+data[i+3][d]
            if col.count('X') + col.count('T') == 4:
                result += 'Case #'+str(index)+': X won'
                found = True
                break
            if col.count('O') + col.count('T') == 4:
                result += 'Case #'+str(index)+': O won'
                found = True
                break

    if found == False:
        col = data[i][0]+data[i+1][1]+data[i+2][2]+data[i+3][3]
        if col.count('X') + col.count('T') == 4:
            result += 'Case #'+str(index)+': X won'
            found = True
           
        if col.count('O') + col.count('T') == 4:
            result += 'Case #'+str(index)+': O won'
            found = True
            

    if found == False:
        col = data[i][3]+data[i+1][2]+data[i+2][1]+data[i+3][0]
        if col.count('X') + col.count('T') == 4:
            result += 'Case #'+str(index)+': X won'
            found = True
            
        if col.count('O') + col.count('T') == 4:
            result += 'Case #'+str(index)+': O won'
            found = True
            

    if found == False:
        if('.' in grid):
            result += 'Case #'+str(index)+': Game has not completed'
        else:
            result += 'Case #'+str(index)+': Draw'

     
    result += '\n'
    index += 1

result = result.strip('\n')
  
print(result)

f = open('A-large.out','w')
f.write(result)
f.close()
