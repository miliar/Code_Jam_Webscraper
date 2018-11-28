f = open('A-small-attempt1.in')
lines = [i.strip() for i in f.readlines()]

number_of_tricks = lines[0]

for i in range(int(number_of_tricks)):
    board = {1:[],2:[]}
    board_line_index = {1:(i*10)+1,2:(i*10)+1+5}
    guess = {1:int(lines[board_line_index[1]]), 2:int(lines[board_line_index[2]])}
    for b in board:
        for j in range(4):
            board[b].append(lines[board_line_index[b]+j+1])
#     print guess
#     print board
    row1 = board[1][guess[1]-1].split(' ')
    row2 = board[2][guess[2]-1].split(' ')
    
    
    
    
    repeat_count = 0
    picked_number = None
    for q in row1:
        if q in row2:
            repeat_count += 1
            picked_number = q
#             print "Q",q
    
    if repeat_count == 0:
        result = "Volunteer cheated!"
    elif repeat_count == 1:
        result = picked_number
    else:
        result = 'Bad magician!'
        
    print "Case #{}: {}".format(i+1,result)
#     print repeat_count
#     print row1
#     print row2
#     print "" 
    