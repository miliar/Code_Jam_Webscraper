
    
def get_output(case, lst):
    if lst[1] == 1:
        if lst[2]==1:
            if lst[0]== 1:
                return "Case #%d: %s\n" %(case, "GABRIEL")
            else:
                return "Case #%d: %s\n" %(case, "RICHARD")
        elif lst[2] == 2:
            if lst[0]== 1 or lst[0] == 2:
                return "Case #%d: %s\n" %(case, "GABRIEL")
            else:
                return "Case #%d: %s\n" %(case, "RICHARD")
        elif lst[2] == 3:
            if lst[0] == 1:
                return "Case #%d: %s\n" %(case, "GABRIEL")
            else:
                return "Case #%d: %s\n" %(case, "RICHARD")
        elif lst[2] == 4:
            if lst[0] == 1 or lst[0] == 2:
                return "Case #%d: %s\n" %(case, "GABRIEL")
            else:
                return "Case #%d: %s\n" %(case, "RICHARD")
    if lst [1] == 2:
        if lst[2] == 2:
            if lst[0] == 2 or lst[0] == 1:
                return "Case #%d: %s\n" %(case, "GABRIEL")
            else:
                return "Case #%d: %s\n" %(case, "RICHARD")
        elif lst[2] == 3:
            if lst[0] == 4:
                return "Case #%d: %s\n" %(case, "RICHARD")
            else:
                return "Case #%d: %s\n" %(case, "GABRIEL")
        elif lst[2] == 4:
            if lst[0] == 1 or lst[0] == 2:
                return "Case #%d: %s\n" %(case, "GABRIEL")
            else:
                return "Case #%d: %s\n" %(case, "RICHARD")        
    if lst[1] == 3:
        if lst[2] ==3:
            if lst[0]== 2 or lst[0] == 4:
                return "Case #%d: %s\n" %(case, "RICHARD") 
            if lst[0] == 1 or lst[0] == 3:
                return "Case #%d: %s\n" %(case, "GABRIEL") 
        else:
            return "Case #%d: %s\n" %(case, "GABRIEL") 
    if lst[1] == 4:
        if lst[0] == 3:
            return "Case #%d: %s\n" %(case, "RICHARD")
        return "Case #%d: %s\n" %(case, "GABRIEL") 
        
        
def main():
    text_file = open("D-small-attempt7.in")
    lines = text_file.readlines()
    text_file.close()
    output = open('output.txt', 'w')
    for i in range(int(lines[0]) + 1)[1::]:
        lst = []
        for x in lines[i].split():
            lst.append(int (x))
        if lst[1] > lst[2]:
            j = lst[1]
            lst[1] = lst[2]
            lst[2] = j 
        output.write(get_output(i, lst))
    return

    
if __name__ == "__main__":
    
    main()