with open("A-small-attempt2.in", "rt") as text:
    size = int(text.readline());
    input = text.read().split("\n");

output = open("A-small.out", "wt");
    
#guess state: set of state_1 row n union set of state_2 column m has one and only one element
#bad magician state: multiple solutions
#cheated state: no solutions

for i in range(0,size):
    row1 = int(input[10 * i]) - 1;
    table_1 = [input[10 * i + 1].split(), input[10 * i + 2].split(), input[10 * i + 3].split(),input[10 * i + 4].split()];
    row2 = int(input[10 * i + 5]) - 1;
    table_2 = [input[10 * i + 6].split(), input[10 * i + 7].split(), input[10 * i + 8].split(),input[10 * i + 9].split()];
    count = 0;
    for y in range(0,4):
        for x in range(0,4):
            if table_1[row1][x] == table_2[row2][y]:
                count = count + 1;
                value = table_1[row1][x];
            if count > 1:
                break;
        else:
            continue;
    if count == 0:
        output.write("Case #" + str(i + 1) + ": Volunteer cheated!\n");
    elif count == 1:
        output.write("Case #" + str(i + 1) + ": " + value + "\n");
    elif count > 1:
        output.write("Case #" + str(i + 1) + ": Bad magician!" + "\n");

output.close();
