f = open('input.in', 'r')
f2 = open('output2.out', 'w')

def write(output):
    print(output, end="")
    f2.write(output)

test_cases = int(f.readline())
for test_case in range(test_cases):
    selection_1 = int(f.readline())
    #print("selection_1", selection_1)
    
    rows = []
    rows.append(f.readline().split())
    rows.append(f.readline().split())
    rows.append(f.readline().split())
    rows.append(f.readline().split())
    row_1 = rows[selection_1-1]
    #print("row_1", row_1)
    
    selection_2 = int(f.readline())
    #print("selection_2", selection_1)
    rows = []
    rows.append(f.readline().split())
    rows.append(f.readline().split())
    rows.append(f.readline().split())
    rows.append(f.readline().split())
    row_2 = rows[selection_2-1]
    #print("row_2", row_2)
    
    r = set(row_1).intersection( set(row_2) )
    #print("r",r)
    if len(r) is 1:
        write("case #"+str(test_case+1)+": "+ r.pop())
    elif len(r) is 0:
        write("case #"+str(test_case+1)+": Volunteer cheated!")
    else:
        write("case #"+str(test_case+1)+": Bad magician!")
    write("\n")
    
print("Done")
            
            
            
