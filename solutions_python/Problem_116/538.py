#0 - Draw
#1 - X won
#2 - O won
#3 - Game has not completed
def verify_winner(x, o , t, dot, prev_ret):
    if x + t == 4:
        return 1
    if o + t == 4:
        return 2
    if dot > 0:
        return 3
    
    if prev_ret == 3:
        return 3    
    return 0
    
    
def check_count(elem, x, o, t, dot):
    if elem == 'X':
        x = x + 1
    elif elem == 'O':
        o = o + 1
    elif elem == 'T':
        t = t + 1
    elif elem == '.':
        dot = dot + 1
    return x, o, t, dot

def winner(input_data):
    ret_value = 0
    for row in xrange(4):
        x = 0
        o = 0
        t = 0
        dot = 0
        for col in xrange(4):
            x, o, t, dot = check_count(input_data[row][col], x, o, t, dot)
            
        ret_value = verify_winner(x, o , t, dot, ret_value)
        if ret_value == 1:
            return 'X won'
        elif ret_value == 2:
            return 'O won'
               
    for col in xrange(4):
        x = 0
        o = 0
        t = 0
        dot = 0
        for row in xrange(4):
            x, o, t, dot = check_count(input_data[row][col], x, o, t, dot)
        ret_value = verify_winner(x, o , t, dot, ret_value)
        if ret_value == 1:
            return 'X won'
        elif ret_value == 2:
            return 'O won'
    
    row = 0
    col = 0
    x = 0
    o = 0
    t = 0
    dot = 0
    while row < 4:
          x, o, t, dot = check_count(input_data[row][col], x, o, t, dot)
          row = row + 1
          col = col + 1
    ret_value = verify_winner(x, o , t, dot, ret_value)
    if ret_value == 1:
        return 'X won'
    elif ret_value == 2:
        return 'O won'
        
    row = 0
    col = 3
    x = 0
    o = 0
    t = 0
    dot = 0
    while row < 4:
          x, o, t, dot = check_count(input_data[row][col], x, o, t, dot)
          row = row + 1
          col = col - 1
    ret_value = verify_winner(x, o , t, dot, ret_value)
    if ret_value == 1:
        return 'X won'
    elif ret_value == 2:
        return 'O won'
        
    if ret_value == 3:
        return 'Game has not completed'
                
    return "Draw"
  
def parse_file(input_file):
    T = int(input_file.readline().replace('\n',''))        
    out_file = file("A-large.out", "w")        
    for counter in xrange(T):
        input_data = []
        for i in xrange(4):
            str_read = input_file.readline().replace('\n','')
            row = []
            for j in xrange(len(str_read)):
                row.append(str_read[j])
                
            input_data.append(row)
        input_file.readline()
        
        out_file.write("Case #"+str(counter+1)+": " + winner(input_data) + "\n") 
        
    out_file.close()
    
if __name__ == "__main__":
    input_file = file("A-large.in")
    parse_file(input_file)
