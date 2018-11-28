from sets import Set
import sys

#lines = [line.strip() for line in open("A-small-attempt0.in")]
lines = [line.strip() for line in open(sys.argv[1])]
output_file = open( "sub-1.out", "w" )

testcases = int(lines[0])

i = 1
for t in range(1, testcases + 1):
    row_number = int(lines[i])
    for row in range(1, 5):
        if row_number == row :
            set1 = Set(lines[row + i].split())
        
    i += 5
    row_number = int(lines[i])
    for row in range(1, 5):
        if row_number == row:
            set2 = Set(lines[row + (i)].split())
    
    i += 5
    
    result = "Case #" + str(t) + ": "
    combination = set1 & set2

    if len(combination) == 0:
        result += "Volunteer cheated!";
    elif len(combination) == 1:
        result += combination.pop();
    else:
        result += "Bad magician!";
        
    output_file.write(result + "\n")
    print(result)
    
output_file.close()