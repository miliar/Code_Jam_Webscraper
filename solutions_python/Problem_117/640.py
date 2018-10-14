from copy import deepcopy

def check_row_1(field, row):
    for j in range(len(field[row])):
        if(field[row][j] != 1):
            return False
    return True
    
def check_col_1(field, col):
    for i in range(len(field)):
        if(field[i][col] != 1):
            return False
    return True
    
    
def check_induced_row_1(field, row):
    for j in range(len(field[row])):
        if(field[row][j] == 1 and not check_col_1(field, j)):
            return False
    return True
    
def check_induced_col_1(field, col):
    for i in range(len(field)):
        if(field[i][col] == 1 and not check_row_1(field, i)):
            return False
    return True
    
def check_inner_field_1(field):
    for i in range(1, len(field)-1):
        for j in range(1, len(field[0])-1):
            if(field[i][j] == 1 and \
              (not check_row_1(field, i) and not check_col_1(field, j))):
                return False
    return True
                

def check_pattern(goal):
    corners = [goal[0][0], goal[0][-1], goal[-1][0], goal[-1][-1]]
    row_corners = [goal[0][-1], goal[0][0], goal[-1][-1], goal[-1][0]]
    col_corners = [goal[-1][0], goal[-1][-1], goal[0][0], goal[0][-1]]
    
    answer = True
    
    nb_ones = sum([c == 1 for c in corners])

    # Check corners and induced row/col
    if nb_ones == 1 :
        return False
        
    if nb_ones == 0:
        answer = answer and check_induced_row_1(goal, 0)
        answer = answer and check_induced_row_1(goal, -1)
        answer = answer and check_induced_col_1(goal, 0)
        answer = answer and check_induced_col_1(goal, -1)
        
    elif nb_ones == 1 :
        return False
        
    elif nb_ones == 2 :
        if corners[0] == 1 and corners[1] == 1 :
            answer = answer and check_row_1(goal, 0)
            answer = answer and check_induced_row_1(goal, -1)
            answer = answer and check_induced_col_1(goal, 0)
            answer = answer and check_induced_col_1(goal, -1) 
        elif corners[2] == 1 and corners[3] == 1 :
            answer = answer and check_induced_row_1(goal, 0)
            answer = answer and check_row_1(goal, -1)
            answer = answer and check_induced_col_1(goal, 0)
            answer = answer and check_induced_col_1(goal, -1) 
        elif corners[0] == 1 and corners[2] == 1 :
            answer = answer and check_col_1(goal, 0)
            answer = answer and check_induced_row_1(goal, 0)
            answer = answer and check_induced_row_1(goal, -1)
            answer = answer and check_induced_col_1(goal, -1) 
        elif corners[2] == 1 and corners[1] == 1 :
            answer = answer and check_col_1(goal, -1)
            answer = answer and check_induced_row_1(goal, 0)
            answer = answer and check_induced_row_1(goal, -1)
            answer = answer and check_induced_col_1(goal, 0) 
        else :
            return False
                
    elif nb_ones == 3 :
        if corners[1] == 1 and corners[2] == 1 and corners[3] == 1 :
            answer = answer and check_row_1(goal, -1)
            answer = answer and check_col_1(goal, -1)
            answer = answer and check_induced_row_1(goal, 0)
            answer = answer and check_induced_col_1(goal, 0) 
        elif corners[0] == 1 and corners[2] == 1 and corners[3] == 1 :
            answer = answer and check_row_1(goal, -1)
            answer = answer and check_col_1(goal, 0)
            answer = answer and check_induced_row_1(goal, 0)
            answer = answer and check_induced_col_1(goal, -1)  
        elif corners[0] == 1 and corners[1] == 1 and corners[3] == 1 :
            answer = answer and check_row_1(goal, 0)
            answer = answer and check_col_1(goal, -1)
            answer = answer and check_induced_row_1(goal, -1)
            answer = answer and check_induced_col_1(goal, 0) 
        elif corners[0] == 1 and corners[1] == 1 and corners[2] == 1 :
            answer = answer and check_row_1(goal, 0)
            answer = answer and check_col_1(goal, 0)
            answer = answer and check_induced_row_1(goal, -1)
            answer = answer and check_induced_col_1(goal, -1) 
    
    elif nb_ones == 4 :
        if (check_row_1(goal, 0) and check_row_1(goal, -1)):
            answer = answer and (check_col_1(goal, 0) or check_induced_col_1(goal, 0))
            answer = answer and (check_col_1(goal, -1) or check_induced_col_1(goal, -1))
        elif (check_col_1(goal, 0) and check_col_1(goal, -1)):
            answer = answer and (check_row_1(goal,0) or check_induced_row_1(goal, 0))
            answer = answer and (check_row_1(goal,-1) or check_induced_row_1(goal, -1))
        else :
            return False
    
    return answer and check_inner_field_1(goal)
        

with open("B-small-attempt1.in") as f:
    for turn in range(1, int(f.readline())+1) :
        l = f.readline().split()
        height, width = int(l[0]), int(l[1])
        
        goal = [[2]*width for i in range(height)]
        
        for x in range(height):
            l = f.readline().split()
            for y in range(width):
                goal[x][y] = int(l[y])

        if height == 1 or width == 1 :
            print "Case #%d:" %turn, "YES"
            continue

        if check_pattern(goal) :
            print "Case #%d:" %turn, "YES"
        else :
            print "Case #%d:" %turn, "NO"