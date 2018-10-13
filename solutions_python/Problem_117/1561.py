input_file = open('C:\Programs\programing\python26\contest2013\B-small-attempt0.in', 'r')
output_file = open('C:\Programs\programing\python26\contest2013\B-small-attempt0.out', 'w')

number_inputs = 0
current_input = 1
lines_left = 0
columns,rows = 0,0
field = []
result =""

def is_bad(field,num):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == num:
                return True
    return False

def find_lines(field,num):
    rows =[]
    columns =[]
    for i in range(len(field)):
        counter = 0
        for j in range(len(field[0])):
            if field[i][j] == num:
                counter += 1
            else:
                break
        if counter == len(field[0]):
            rows.append(i)

    for i in range(len(field[0])):
        counter = 0
        for j in range(len(field)):
            if field[j][i] == num:
                counter += 1
            else:
                break
        if counter == len(field):
            columns.append(i)
    return [rows,columns]

def fill_lines(field,rows, columns):
    for i in rows:
        for j in range(len(field[0])):
            field[i][j] += 1

    for i in columns:
        for j in range(len(field)):
            field[j][i] += 1
    return field
    

for line in input_file:
    if number_inputs==0:
        number_inputs = int(line)
    elif line == '\n':
        pass
    elif lines_left == 0:
        t = line.split()
        [rows,columns] = int(t[0]),int(t[1])
        lines_left = rows
        field = []
    else:
        lines_left -= 1
        field_row = []
        t = line.split()
        for ti in t:
            field_row.append(int(ti))
        field.append(field_row)
        if lines_left == 0:
            min_val, max_val = 100,0
            for v in field:
                min_val=min(min_val,min(v))
                max_val=max(max_val,max(v))
            
            for i in range(min_val,max_val):
                lines = find_lines(field,min_val)
                field = fill_lines(field,lines[0],lines[1])
                if(is_bad(field,min_val)):
                    result = "NO"
                    break
            if result != "NO":
                result = "YES"
            output_file.write('Case #' + str(current_input) + ': ' + result)
            if current_input != number_inputs:
                current_input += 1
                output_file.write('\n')
            result =""
        
input_file.close()
output_file.close()
