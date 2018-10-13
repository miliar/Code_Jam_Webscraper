def trick():
    def guess(row1, row2):
        match = []
        for i in row1:
            for j in row2:
                if (i==j):
                    match.append(i)
        if (len(match)==0):
            return 'Volunteer cheated!'
        elif (len(match)==1):
            return str(match[0])
        else:
            return 'Bad magician!'
    global inp, line_counter
    row1_index = int(inp[line_counter])
    line_counter+=1
    rows = []
    for i in range(4):
        rows.append(inp[line_counter])
        line_counter+=1
    row1=[]
    for str_i in rows[row1_index-1].split(' '):
        row1.append(int(str_i))
        
    row2_index = int(inp[line_counter])
    line_counter+=1
    rows = []
    for i in range(4):
        rows.append(inp[line_counter])
        line_counter+=1
    row2=[]
    for str_i in rows[row2_index-1].split(' '):
        row2.append(int(str_i))
    return guess(row1, row2)

with open('A-small-attempt3.in', 'r') as f:
    inp = f.readlines()
    f.close()
line_counter = 0
T = int(inp[line_counter])
line_counter+=1
data = ''
for i in range(T):
    data += 'Case #%d:' %(i+1) + ' ' + trick()+'\n'
with open('output.txt', 'w') as f:
    f.write(data)
    f.close()
print data
