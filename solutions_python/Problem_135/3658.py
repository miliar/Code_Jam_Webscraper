
if __name__ == "__main__":
    inputfile = open("input.in", "r");
    length = inputfile.readline();
    
    output = open("output.txt", "w");

    numbers = [];
    index = 1;
    for i in range(0, int(length) * 2):
        row = int(inputfile.readline());
        for n in range(0, row - 1):
            inputfile.readline();
        line = inputfile.readline();
        line = line.replace("\n", "");
        numbers.append(line.split(" "));
        for k in range(0, 4 - row):
            inputfile.readline();
            
        if (i % 2 <> 0):
            count = 0;
            number = -1;
            for i in range(0, 4):
                for n in range(0, 4):
                    if (numbers[0][n] == numbers[1][i]):
                        count = count + 1;
                        number = numbers[0][n];
                        break;
            casenum = "Case #" + str(index) + ": ";
            if (count >= 2):
                output.write(casenum + "Bad magician!\n");
            elif (number == -1):
                output.write(casenum + "Volunteer cheated!\n");
            else:
                output.write(casenum + str(number) + "\n");
            
            count = 0;
            numbers = [];
            index = index + 1;
            
    output.close();
        
