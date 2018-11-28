import math

# filename = "03-input-test-0"
filename = "03-C-small-attempt6"
# filename = "02-B-large"
fi = open(filename+'.in', 'r')
# lData = list()
debug = True
collect = ""
index = 0
strVal = 0

# R=0
# C=0
# M=0
cases = []

for line in fi:
	if (index > 0):
		line_split = line.strip().split(' ')
		cases.append((int(line_split[0]),int(line_split[1]),int(line_split[2])))

	index = index + 1

fi.close()
# print cases

# Task
def sweep(R, C, M):
    # field_row = "*"*C
    # minefield = (field_row + "\n")*R
    mf_matrix = []
    for i in range(R):
        mf_matrix.append([0]*C)
    print mf_matrix

    # for row in range(R):
    #     for col in range(C):
    #         mf_matrix[row][col] = 0
        # print "Bingo", R, C, M

    # When no mines
    if (0 == M):
        return drawSweeper(R, C, mf_matrix)

    # When only one space for click
    if (1 == R*C-M):
        mf_matrix = []
        for i in range(R):
            mf_matrix.append([-1]*C)
        return drawSweeper(R, C, mf_matrix)

    # Imposible detection
    if ((1 < R*C-M < 4) or (R*C-M ==5) or (R*C-M ==7)) and (R > 1) and (C > 1):
        return "Impossible\n"

    # Two lines left
    if (R == 2) or (C == 2):
        if (M % 2 == 0):
            pass
        else: 
            return "Impossible\n"

    # When 1 line
    if (R == 1) or (C == 1):
        spr = ""
        length = C
        if (C == 1):
            spr = "\n"
            length = R
        return ("c"+spr)+("."+spr)*(length-M-1)+("*"+spr)*(M-1) + "*\n" 

    # Detect square to fill
    # new_square = (R,C,M)
    fill_vertical = True
    new_C = C
    new_R = R
    mines_left = M
    if (M > R) or (M > C):
        if (R > C):
            mines_left = M % C
            new_R = R - ((M - mines_left) / C)
            fill_vertical = False
        else:
            mines_left = M % R
            new_C = C - ((M - mines_left) / R)
            
    #     side_len = int(math.floor(math.sqrt(R*C-M)))
    #     if (side_len*side_len > R*C-M):
    #         new_square = (side_len,side_len,M-R*C+side_len*side_len) 
    #     else: 
    #         new_square = (side_len,side_len+1,M-R*C+side_len*(side_len+1))   
    new_square =  (new_R, new_C, mines_left)
    
    # print "1::",mf_matrix
    # if (R != new_R) or (C != new_C):
    #     for nr in (range(R) if (R == new_R) else range(new_R, R)):
    #         for nc in (range(C) if (C == new_C) else range(new_C)):
    #             mf_matrix[nr][nc] = -1
    # print "2::",mf_matrix

    # One shortest line left
    if (new_C*new_R-mines_left < 4):
        return "Impossible\n"

    # minefield = ("."*new_C + "*"*(C-new_C) + "\n")*new_R 
    # minefield += ("."*(C-new_C) + "*"*new_C + "\n")*(R-new_R)

    mines_left = M
    small_dim = C if (C < R) else R
    large_dim = R if (C < R) else C
    for vert in range(small_dim):
    
        if (C > 2) and (R > 2) and (C*R-M == 4):
            mf_matrix = []
            for i in range(R):
                mf_matrix.append([-1]*C)
            mf_matrix[R-1][C-1] = 0
            mf_matrix[R-2][C-1] = 0
            mf_matrix[R-1][C-2] = 0
            mf_matrix[R-2][C-2] = 0
            
            mines_left = 0
            break
        
        if ((M % C == 0) and (M % R == 0) and (C < R)): # case 1
            for x in range(large_dim*C): 
                if (mines_left == 0):
                    break
                mf_matrix[int(math.floor(x/C))][x%C] = -1
                mines_left -= 1
        elif (M % R == 0):
            for x in range(large_dim*R):
                if (mines_left == 0):
                    break
                mf_matrix[x%R][int(math.floor(x/R))] = -1
                mines_left -= 1
        elif (M % C == 0): # necessary duplications to fit case 1
            for x in range(large_dim*C):
                if (mines_left == 0):
                    break
                mf_matrix[int(math.floor(x/C))][x%C] = -1
                mines_left -= 1
        else:
            if (mines_left-vert+1 == C) or (mines_left-vert+1 == C-2):
                for y in range(vert,R):
                    if (mines_left == 0):
                        break
                    if (y == (R - 2)) and (mines_left == 1):
                        break
                    else:
                        if (mf_matrix[y][vert] == -1):
                            print "Error: duplicate bomb"
                        mf_matrix[y][vert] = -1
                        mines_left -= 1

                for x in range(vert+1,C):
                    if (mines_left == 0):
                        break
                    if (x == (C - 2)) and (mines_left == 1):
                        break # corner case
                    else:
                        if (mf_matrix[vert][x] == -1):
                            print "Error: duplicate bomb"
                        mf_matrix[vert][x] = -1
                        mines_left -= 1

            else:
                for x in range(vert,C):
                    if (mines_left == 0):
                        break
                    if (x == (C - 2)) and (mines_left == 1):
                        break # corner case
                    else:
                        if (mf_matrix[vert][x] == -1):
                            print "Error: duplicate bomb"
                        mf_matrix[vert][x] = -1
                        mines_left -= 1

                for y in range(vert+1,R):
                    if (mines_left == 0):
                        break
                    if (y == (R - 2)) and (mines_left == 1):
                        break # corner case, check 149, 169,174, 177, 198, 200, 203
                        # break didnt fix: 200,198,174,69 
                        # mod didnt fix: 200,198 
                        # Attemp 2
                        # broke 111
                        # impossible broke 215,213,210
                        # Attemp3
                        # broke 9
                        # Attemp4
                        # broke 79
                        # Attemp5
                        # broke 31
                    else:
                        if (mf_matrix[y][vert] == -1):
                            print "Error: duplicate bomb"
                        mf_matrix[y][vert] = -1
                        mines_left -= 1



    # mf_matrix[1][0] = -1
    # mf_matrix[0][1] = -1

    # print "Range", vert, range(vert,C), range(vert+1,R)
    # print mines_left, drawSweeper(R, C, mf_matrix)

    # print "Square", new_square, "Verticlal", fill_vertical
    minefield = ""
    minefield = drawSweeper(R, C, mf_matrix)
    
    # left_mines = 0
    # left_cord = (0,0)
    # if (R < C):
    #     left_mines = M % R
    #     left_cord = (C - (M-left_mines)/R, R)
    # elif (R >= C):
    #     left_mines = M % C
    #     left_cord = (C, R - (M-left_mines)/C)

    # print "Mines", left_mines, "Cords", left_cord

    return minefield

def drawSweeper(R, C, matrix):
    print matrix
    line = ""
    for row in range(R):
        for col in range(C):
            if (row == R - 1) and (col == C - 1):
                line += "c"
            else:
                line += str('.' if (matrix[row][col] >= 0) else "*")
        line += "\n"
    return line

index = 1
solution = ""
for case in cases:
    # solution = solution +  "Case"+str(index)+": "+str(case[0])+","+ str(case[1])+","+ str(case[2])+"\n"
    solution = solution + "Case #" + str(index) + ":\n" + sweep(case[0], case[1], case[2])
    index = index + 1

print solution

fo = open(filename+'.out', 'w')
solution = solution.strip()
fo.write(solution)
fo.close()