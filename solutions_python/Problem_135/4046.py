input = open("test.input").readline

T = int(input())

for x in range(T):
    choice1 = int(input()) - 1
    board1 = [ input().strip().split(" ") for i in range(4)]

    choice2 = int(input()) - 1
    board2 = [ input().strip().split(" ") for i in range(4)]

    row1, row2 = board1[choice1], board2[choice2]
    count, element = 0, None
    
    for i in range(4):
        for j in range(4):
            if row1[i] == row2[j]:
                count += 1
                element = row1[i]
                
    print("Case #%d: %s" % (x + 1, (element if count == 1 else "Bad magician!" if count > 1 else "Volunteer cheated!")))
