#read input and setup output file
text = open("A-smaller-practice.in");
data = text.read().split("\n");
outputfile = open("output.txt", "w");
outputfile.write("");

#get cases amount
cases = int(data[0]);
data.pop(0);

#algorithm here

directions = [-1, -1, 0, -1, 1, -1, 1, 0, 1, 1, 0, 1, -1, 1, -1, 0];
rowy = 0;
for i in range(0, cases):
    game = data[rowy] + data[rowy + 1] + data[rowy + 2] + data[rowy + 3];
    gamefinish = False;
    draw = True;
    output = "";
    for y in range(0, 4):
        for x in range(0, 4):
            key = game[y * 4 + x];

            if (key == "."):
                draw = False;
                
            if (key == "." or key == "T"):
                continue;

            #search in all directions for a match
            rowx = 0;
            found = False;
            for d in range(0, len(directions) / 2):
                for n in range(1, 4):
                    num = (y + (directions[rowx + 1] * n)) * 4 + (x + (directions[rowx] * n));
                    if (num < 16 and num >= 0):
                        if (game[num] == key or n >= 4 and game[num] == "T"):
                            if (n >= 3):
                                found = True;
                                break;
                        else:
                            break;
                    else:
                        break;
                            
                    if (found):
                        break;
                    
                rowx += 2;
                if (found):
                    break;
                
            if (found):
                gamefinish = True;
                output = "Case #" + str(i + 1) + ": " + key + " won";
                break;
                
        if (gamefinish):
            break;

    if (gamefinish == False):
        if (draw):
            output = "Case #" + str(i + 1) + ": " + "Draw";
        else:
            output = "Case #" + str(i + 1) + ": " + "Game has not completed";

    print output;
    outputfile.write(output + "\n");
    
    rowy += 5;

#end algorithm


#close output file
outputfile.close();

