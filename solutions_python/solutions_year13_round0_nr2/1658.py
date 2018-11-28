##raw_input = """3
##3 3
##2 1 2
##1 1 1
##2 1 2
##5 5
##2 2 2 2 2
##2 1 1 1 2
##2 1 2 1 2
##2 1 1 1 2
##2 2 2 2 2
##1 3
##1 2 1"""

input_file = open('B-large.in','r')
raw_input = input_file.read()

lines = raw_input.split('\n')

num_cases = int(lines[0])
case_num = 1

output_text = ''
output_file = open('lawnmower_output.txt','w')

case_start_line = 1
while case_num<=num_cases:
    num_rows = int(lines[case_start_line].split(' ')[0])
    num_cols = int(lines[case_start_line].split(' ')[1])

    rows = lines[case_start_line+1 : case_start_line+1+num_rows] #inclusive of start, not end

    lawn=[]

    for row in rows:
        cells=[]
        for cell in row.split(' '):
            cells.append(int(cell))  #list of ints for row instead of str
        #print(cells)
        lawn.append(cells) #create 2D array of ints

    #print(lawn)

    row_maxes = list(map(max,lawn))
    col_maxes = list(map(max,zip(*lawn))) #zip() transposes
    #print(list(row_maxes))
    #print(list(col_maxes))

    doable='YES'
    for r in range(0,num_rows):
        for c in range(0,num_cols):
            if lawn[r][c]!=row_maxes[r] and lawn[r][c]!=col_maxes[c]:
                doable='NO'

    #print('Case #'+str(case_num)+': '+doable)
    output_text = output_text+'Case #'+str(case_num)+': '+doable+'\n'

    case_start_line += num_rows+1
    case_num += 1

output_file.write(output_text)
output_file.close()
print(output_text)
