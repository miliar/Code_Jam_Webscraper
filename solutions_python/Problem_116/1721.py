def convert_input(a, b, c, d):
    result_list = []
    result_list.append(list(a))
    result_list.append(list(b))
    result_list.append(list(c))
    result_list.append(list(d))

    return result_list


def check_horizontal_won(a):
    for i in range(0, 4):
        x_num = 0
        o_num = 0
        t_num = 0

        for j in range(0, 4):
            if(a[i][j]=='X'):
                x_num += 1
            elif(a[i][j]=='O'):
                o_num += 1
            elif(a[i][j]=='T'):
                t_num += 1
        if (x_num == 4) or ((x_num + t_num) == 4):
            return "X won"
        elif (o_num == 4) or ((o_num + t_num) == 4):
            return "O won"
    return False

def check_vertical_won(a):
    for i in range(0, 4):
        x_num = 0
        o_num = 0
        t_num = 0

        for j in range(0, 4):
            if(a[j][i]=='X'):
                x_num += 1
            elif(a[j][i]=='O'):
                o_num += 1
            elif(a[j][i]=='T'):
                t_num += 1
        if (x_num == 4) or ((x_num + t_num) == 4):
            return "X won"
        elif (o_num == 4) or ((o_num + t_num) == 4):
            return "O won"
    return False
def check_diagonal_won(a):
        x_num = 0
        o_num = 0
        t_num = 0

        for i in range(0, 4):
            if(a[i][i]=='X'):
                x_num += 1
            elif(a[i][i]=='O'):
                o_num += 1
            elif(a[i][i]=='T'):
                t_num += 1
        if (x_num == 4) or ((x_num + t_num) == 4):
            return "X won"
        elif (o_num == 4) or ((o_num + t_num) == 4):
            return "O won"
        else:
            
            x_num = 0
            o_num = 0
            t_num = 0
            i = 0
            j = 3
            while i<=3:
                if(a[i][j]=='X'):
                    x_num += 1
                elif(a[i][j]=='O'):
                    o_num += 1
                elif(a[i][j]=='T'):
                    t_num += 1
                i = i + 1
                j = j - 1
            if (x_num == 4) or ((x_num + t_num) == 4):
                return "X won"
            elif (o_num == 4) or ((o_num + t_num) == 4):
                return "O won"
        return False

def check_any_dot(a):
    
    dot_num = 0
        
    for i in range(0, 4):
        for j in range(0, 4):
            if(a[i][j]=='.'):
                dot_num += 1
  
    return dot_num


def game_func(a):
    result = check_horizontal_won(a) 
    if result != False :
        return result
    else:
        result = check_vertical_won(a)
        if result != False :
            return result
        else:
            result = check_diagonal_won(a)
            if result != False :
                return result
            else:
                dot_num = check_any_dot(a)
                if dot_num != 0:
                    result = "Game has not completed"
                    return result
                else:
                    result = "Draw"
                    return result

input = open('A-large.in', 'r')
T = int(input.readline())
for i in range(0, T):
    text = input.readline()
    a = text.split("\n")[0]
    text = input.readline()
    b = text.split("\n")[0]
    text = input.readline()
    c = text.split("\n")[0]
    text = input.readline()
    d = text.split("\n")[0]
    text = input.readline()

    converted = convert_input(a, b, c, d)
    result = game_func(converted)
    print "Case #" + str(i+1) + ": " + str(result) 
    
