import sys  

#f = open("input.txt", "r")

f = open("A-small-attempt0.in", "r")
#f = open("A-large.in", "r")

sys.stdout = open('A-small-out.txt', 'w')
#sys.stdout = open('A-large-out.txt', 'w')

t = int(f.readline().strip())

for case_num in range(1,t+1):
    input_line = f.readline().strip().split(" ")
    h = int(input_line[0]) #num rows
    w = int(input_line[1]) #num cols
    cake = [["?" for x in range(w)] for y in range(h)] 
    char_dict = {}
    for count in range(0, h):
        row_input = f.readline().strip()
        cake[count] = list(row_input)
        for alphabet in list(row_input):
            if alphabet == "?":
                continue
            if alphabet in char_dict:
                char_dict[alphabet] += 1
            else:
                char_dict[alphabet] = 1

    for alphabet in char_dict:
        min_x = 1000000
        min_y= 1000000
        max_x = 0
        max_y = 0
        for i in range(0,h):
            for j in range(0,w):
                if (cake[i][j] == alphabet):
                    min_x = min(min_x,j)
                    max_x = max(max_x,j)
                    min_y = min(min_y,i)
                    max_y = max(max_y,i)
        #fill in the cake according to the params
        for i in range(min_y,max_y+1):
            for j in range(min_x,max_x+1):
                cake[i][j] = alphabet
                    
        #print ("Alphabet", alphabet, min_x, min_y, max_x, max_y)
    
    for alphabet in char_dict:
        min_x = 1000000
        min_y= 1000000
        max_x = 0
        max_y = 0
        for i in range(0,h):
            for j in range(0,w):
                if (cake[i][j] == alphabet):
                    min_x = min(min_x,j)
                    max_x = max(max_x,j)
                    min_y = min(min_y,i)
                    max_y = max(max_y,i)
        #for each direction, attempt to fill in more cake
        #UPWARDS
        to_fill = True
        while(to_fill):
            i = min_y - 1
            if (i < 0):
                break
            for j in range(min_x,max_x+1):
                if cake[i][j] != "?":
                    to_fill = False
                    break
            if (to_fill):
                for j in range(min_x,max_x+1):
                    cake[i][j] = alphabet
                min_y -= 1

        #DOWNWARDS
        to_fill = True
        while(to_fill):
            i = max_y + 1
            if (i>= h):
                break
            for j in range(min_x,max_x+1):
                if cake[i][j] != "?":
                    to_fill = False
                    break
            if (to_fill):
                for j in range(min_x,max_x+1):
                    cake[i][j] = alphabet
                max_y += 1
        
        #LEFT
        to_fill = True
        while(to_fill):
            j = min_x - 1
            if (j < 0):
                break
            for i in range(min_y, max_y+1):
                if cake[i][j] != "?":
                    to_fill = False
                    break
            if (to_fill):
                for i in range(min_y, max_y+1):
                    cake[i][j] = alphabet
                min_x -= 1

        #RIGHT
        to_fill = True
        while(to_fill):
            j = max_x + 1
            if (j >= w):
                break
            for i in range(min_y, max_y+1):
                if cake[i][j] != "?":
                    to_fill = False
                    break
            if (to_fill):
                for i in range(min_y, max_y+1):
                    cake[i][j] = alphabet
                max_x += 1
    
    #code for iterating through cake by index
    print ("Case #{}:".format(case_num))
    for i in range (0,h):
        for j in range(0,w):
            print (cake[i][j], end="")
        print ()