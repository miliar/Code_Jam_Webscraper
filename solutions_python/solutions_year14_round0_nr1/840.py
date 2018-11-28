T = int(raw_input())

def get_row():
    row_no = int(raw_input())
    
    #seek to that row
    for j in range(row_no-1):
        raw_input()
    row = map(int, raw_input().split())
    
    #skip remaining rows
    for j in range(row_no,4):
        raw_input()
    
    row = set(row)
    return row

def get_output(row1, row2):
    card = row1.intersection(row2)
    
    if len(card) == 0:
        return "Volunteer cheated!"
    elif len(card) > 1:
        return "Bad magician!"
    else:
        return card.pop()
    

for i in range(T):
    
    row1 = get_row()
    row2 = get_row()
    
    output = get_output(row1,row2)
    
    print "Case #%s:" % str(i+1), output