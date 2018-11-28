def square_grid(intlist:list)->list:
    grid_list = []
    counter = 0
    
    for j in range(4):
        row_list = []
        
        for k in range(4):
            element = intlist[counter]
            counter += 1
            
            row_list.append(element)
        
        grid_list.append(row_list)
        
    return grid_list
            
def intersection(sg1:list, sg2:list, r1:int, r2:int)->list:
    intersection_list = []
    l1 = sg1[r1-1]
    l2 = sg2[r2-1]

    for l in range(4):
        e = l1[l]
        
        for m in range(4):
            if l2[m] == e:
                intersection_list.append(e)

    return intersection_list
    
def magic_trick():
    infile = open('input.txt', 'r')
    content = infile.read()
    infile.close()
    grid_list = content.split()

    counter = 0
    T = int(grid_list[0])
    counter += 1
    
    for i in range(T):
        r1 = int(grid_list[counter])
        counter += 1
        
        sg1 = square_grid(grid_list[counter:(counter+16)])
        counter += 16
        
        r2 = int(grid_list[counter])
        counter += 1
        
        sg2 = square_grid(grid_list[counter:(counter+16)])
        counter += 16

        common = intersection(sg1, sg2, r1, r2)

        if len(common) == 1:
            print("Case #" + str(i+1) + ': ' + common[0])
        elif len(common) > 1:
            print("Case #" + str(i+1) + ': ' + "Bad magician!")
        else:
            print("Case #" + str(i+1) + ': ' + "Volunteer cheated!")

def read_file():
    infile = open('input.txt', 'r')
    content = infile.read()
    infile.close()
    grid_list = content.split()

    print(grid_list)
    print(grid_list[0])
    print(len(grid_list[1:17]))
    

#read_file()    

magic_trick()
    

