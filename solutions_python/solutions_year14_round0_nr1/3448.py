T = int(input())
case = 1
final_print = ""
for i in range(T):
    row1_in_integers = []
    row2_in_integers = []
    row1 = int(input())
    for j in range(4):
        row_value = input(str())
        if j == (row1-1):
            row_value += " "
            c = 0        
            for k in range(len(row_value)):
                if row_value[k] == " ":
                     row1_in_integers.append(int(row_value[c:k]))
                     c = k
            
    row2 = int(input())
    for l in range(4):
        row_value = input(str())
        if l == row2 - 1:
            row_value += " "
            c = 0        
            for m in range(len(row_value)):
                if row_value[m] == " ":
                     row2_in_integers.append(int(row_value[c:m]))
                     c = m
            
    count = 0
    number = -1
    for n in range(len(row1_in_integers)):
        for o in range(len(row2_in_integers)):
            if row1_in_integers[n] == row2_in_integers[o]:
                count += 1
                number = row1_in_integers[n]
    if count == 0:
        final_print += "Case #" + str(case) + ": Volunteer cheated!" + "\n"
    elif count == 1:
        final_print += "Case #" + str(case) + ": " + str(number) + "\n"
    elif count > 1:
        final_print += "Case #" + str(case) + ": Bad magician!" + "\n"
    case += 1
print (final_print)
        
    
                     
                    
    
