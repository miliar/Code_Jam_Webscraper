def rotate(l):
    ret = [[0 for x in range(4)] for x in range(4)] 
    for i in range(4):
        for j in range(4):
            ret[i][j] = l[4-j-1][i]
    return ret

def main():
    f = open('small.in', 'r')
    n = f.readline()
    array = []
    for i in range(int(n)):
        array1 = []
        for j in range(4):
            line = f.readline()
            array1.append(list(line.strip("\n\r")))
        array.append(array1)
        line = f.readline()
    f.close()

    f = open('output.txt', 'w')
    for i,temp in enumerate(array):
        x = 0
        o = 0
        point = 0
        # horizontal
        for j in temp:
            cx = j.count('X')
            co = j.count('O')
            ct = j.count('T')
            point += j.count('.')
            if cx+ct == 4:
                x = 1
            if co+ct == 4:
                o = 1
        # vertical
        temp1 = rotate(temp)
        for j in temp1:
            cx = j.count('X')
            co = j.count('O')
            ct = j.count('T')
            if cx+ct == 4:
                x = 1
            if co+ct == 4:
                o = 1
        #diagonals
        list1 = []
        list2 = []
        list1.append(temp[0][0])
        list1.append(temp[1][1])
        list1.append(temp[2][2])
        list1.append(temp[3][3])
        list2.append(temp[0][3])
        list2.append(temp[1][2])
        list2.append(temp[2][1])
        list2.append(temp[3][0])
        cx1 = list1.count('X')
        co1 = list1.count('O')
        ct1 = list1.count('T')
        cx2 = list2.count('X')
        co2 = list2.count('O')
        ct2 = list2.count('T')
        if cx1+ct1 == 4:
            x = 1
        if co1+ct1 == 4:
            o = 1
        if cx2+ct2 == 4:
            o = 1
        if co2+ct2 == 4:
            o = 1
        string = "Case #" + str(i+1) + ": "
        if x == 1:
            string += "X won"
        if o == 1:
            string += "O won"
        if x+o == 0:
            if point > 0:
                string += "Game has not completed"
            else:
                string += "Draw"
        string += "\n"
        f.write(string)
    f.close()

main()
