start_of_case = True
i = 0
cases = []
raise_guide = []
IN = open('B-large.txt','r')
row = 0
col = 0
counter = 0
temp_case =[]
max_value = []
temp_max = 0
min_value = []
temp_min = 101
raise_template = []
for line in IN:
    i += 1
    if (i == 1):
        total_cases = int(line)
    else:
        if(start_of_case):
            start_of_case = False
            data = line.split(" ")
            row = int(data[0])
            col = int(data[1])
            counter = 0
            temp_max = 0
            temp_min = 101
        else:
            counter += 1
            data = line.split(" ")
            temp_row = []
            for datapoint in data:
                temp_row.append(int(datapoint))
                temp_max = max(int(datapoint),temp_max)
                temp_min = min(int(datapoint),temp_min)
            temp_case.append(temp_row)
            if(counter == row):
                start_of_case = True
                cases.append(temp_case)
                temp_case = []
                max_value.append(temp_max)
                min_value.append(temp_min)

x = -1
OUT = open('B-large-out.txt','w')
for i in cases:
    for row in i:
        print row
    x += 1
    raised_line = True
    while(min_value[x] < max_value[x]):        
##        print "---------------------------------------------"
##        print min_value[x]
##        for row in i:
##            print row
        good_rows = []
        good_cols = []
        for row in range(0,len(i)):
            lowest_row = True
            for col in range(0,len(i[row])):
                if(i[row][col] != min_value[x]):
                    lowest_row = False
            if(lowest_row):
                good_rows.append(row)

        for col in range(0,len(i[0])):
            lowest_col = True
            for row in range(0,len(i)):
                if(i[row][col] != min_value[x]):
                    lowest_col = False
            if(lowest_col):
                good_cols.append(col)

##        print good_rows
##        print good_cols

        for row in range(0,len(i)):
            for col in range(0,len(i[row])):
                if(i[row][col] == min_value[x]):
                    if(row in good_rows or col in good_cols):
                       i[row][col] += 1

        min_value[x] += 1

##    print "FINAL"
##    for row in i:
##        print row
##    print "-----------------------------"

    possible_pattern = "YES"
    for row in range(0,len(i)):
        for col in range(0,len(i[row])):
            if(i[row][col] != max_value[x]):
                possible_pattern = "NO"

    print "Case #{0}: {1}\n".format(x+1,possible_pattern)
    OUT.write("Case #{0}: {1}\n".format(x+1,possible_pattern))
OUT.close()
            
