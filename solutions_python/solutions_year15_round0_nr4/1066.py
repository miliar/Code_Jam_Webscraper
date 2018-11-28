
#lines = list(open("input.txt"))
lines = list(open("D-small-attempt1.in"))
print(lines)
outFile = open("output1.txt", "w")

for test in range(1, int(lines.pop(0))+1):
    
    x, r, c = [int(x) for x in lines.pop(0).split()]
    print(test, x, r, c)

    richardWin = True
    if x == 1:
        richardWin = False
    elif x == 2:
        richardWin = (r == 1 and c == 1) or ((r*c % 2) != 0)
    elif x == 3:
        richardWin = (r == 1 or c == 1) or ((r*c % 3) != 0)
    else:
        richardWin = r*c != 12 and r*c != 16

    winner = "RICHARD" if richardWin else "GABRIEL"
    print("winner: ", winner)
    outFile.write("Case #{}: {}\n".format(test, winner))
    
outFile.close()
