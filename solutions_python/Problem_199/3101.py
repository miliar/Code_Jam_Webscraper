#avoloc
def flip(inputline,size):
    line = []
    for c in  inputline:
        line.append(c)
    linelength = len(line)
    solvable = True
    if linelength < size and line.count('-')>0:
        solvable = False
    flips = 0
    for i in range(int((linelength-size+2)/2)):
        if line.count('-') == 0 or solvable == False:
            break
        leftaction = True
        rightaction = True
        if line[i] == '-' and size+i <= linelength:
            flips = flips+1
            for ii in range(0,size):
                if line[i+ii] == '-':
                    line[i+ii] = '+'
                else:
                    line[i+ii] = '-'
        else:
            leftaction = False
        if line[-i-1] == '-' and size+i < linelength:
            flips = flips+1
            for ii in range(0,size):
                if line[-i-1-ii] == '-':
                    line[-i-1-ii] = '+'
                else:
                    line[-i-1-ii] = '-'
        else:
            rightaction = False
    if line.count('-') > 0:
        solvable = False
    if(solvable):
        return(flips)
    else:
        return('IMPOSSIBLE')

t = int(input())
for row in range(1, t+1):
    o = input().split(" ")
    sol = flip(o[0],int(o[1]))
    print("Case #{}: {}".format(row,sol))
