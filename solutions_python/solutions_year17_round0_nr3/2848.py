def FindMaxEmptySpace(list):
    count_index = 0
    start_index = 0
    stop_index = 0
    index = 0
    c = 0
    max = 0
    for l in list:
        if l == 1:
            if c > max:
                max = c
                count_index = index
            c = 0
            index += 1
        if l == 0:
            c += 1

    counter = 0
    for i in range(0,len(list),1):
        if list[i] == 1:
            counter += 1
            if counter == count_index:
                start_index = i+1
                break

    for i in range(start_index,len(list),1):
        if list[i] == 1:
            stop_index = i-1
            break

    return start_index,stop_index

def MaxMinLR(index):
    left = 0
    for i in range(index-1,0,-1):
        if list[i] == 1:
            break
        left += 1
    #print("Left Distance: " + str(left))

    right = 0
    for i in range(index+1,len(list),1):
        if list[i] == 1:
            break
        right += 1
    #print("Right Distance: " + str(right))

    max_lr = max(left, right)
    min_lr = min(left, right)
    return str(max_lr),str(min_lr)

filename = "C:\\Users\\duckarcher\\Downloads\\C-small-1-attempt0.in"
f = open(filename)
f2 = open(filename.replace(".in", ".out"), 'w')
case = 1
for line in f:
    if " " in line:
        line = line.strip("\n")
        print("Trying line: " + line)
        stalls = int(line.split(" ")[0])
        people = int(line.split(" ")[1])
        list = [0] * (stalls+2)
        list[0] = 1
        list[len(list)-1] = 1
        #list[2] = 1
        #list[3] = 1
        #for i in list:
            #print(i)
        for i in range (0,people,1):
            [start_empty,stop_empty] = FindMaxEmptySpace(list)
            #print("Max Empty Space: " + str(start_empty) + ":" + str(stop_empty))
            index = int( (start_empty + stop_empty) / 2 )
            list[index] = 1
            [m, n] = MaxMinLR(index)
        out = "Case #" + str(case) + ": " + m + " " + n + "\n"
        print(out)
        f2.write(out)
        case += 1