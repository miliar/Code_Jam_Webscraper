#f = open('test.txt', 'r')
f = open('D-small-attempt5.in', 'r')

cases = int(f.readline())

#richard is choosing the pieces
#gabriel is playing



for case in range(cases):
    temp = f.readline().rstrip('\n')
    info = [int(e) for e in temp.split(" ")]
    answer = ""
    
    xomino = info[0]
    height = info[1]
    width = info[2]
    

    if (width * height) % xomino != 0:
        answer = "RICHARD"
        #print("1")

    elif width * height / xomino == 2 and xomino >= min(height, width) + 2:
        answer = "RICHARD"
        #print("6")
        
    elif xomino % 2 == 1 and (xomino // 2 + 1 > width or xomino // 2 + 1> height):
        answer = "RICHARD"
        #print("2")

    elif xomino > 2 and xomino % 2 == 0 and (xomino / 2 > width or xomino / 2 > height):
        answer = "RICHARD"
        #print("3")
        
    elif xomino > height and xomino > width:
        answer = "RICHARD"
        #print("4")

    elif xomino > 6:
        answer = "RICHARD"
        #print("5")
    
    else:
        answer = "GABRIEL"

    #print(info)
    
    print("Case #"+str(case+1)+": "+answer)
