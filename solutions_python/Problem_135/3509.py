
def readFile(path):
    fh = open(path, "r")
    return fh.readlines()

def writeLinesToFile(lines,path):
    fh = open(path, "w")
    fh.writelines(lines)
    fh.close()


input_path = "D:/jam/2014/task1/test.in"
output_path = "D:/jam/2014/task1/test.out"   
    
lines = readFile(input_path)

test_cases = int(lines[0])
results = [0 for x in range(test_cases)]

 
for i in range(test_cases):
    current_test = i
    linenumber_of_choice1 = int(lines[current_test*10+1])
    linenumber_of_choice2 = int(lines[current_test*10+6])
    row1 = lines[current_test*10+linenumber_of_choice1+1]
    row2 = lines[current_test*10+linenumber_of_choice2+6]
    row1_int = row1.split(" ")
    row2_int = row2.split(" ")
    possible_cards = 0
    correct_choice = 0 
    for j in range (len(row1_int)):
        for k in range(len(row2_int)):
            if int(row1_int[j]) == int(row2_int[k]):
                correct_choice = int(row1_int[j])
                possible_cards += 1
    if (possible_cards == 0):
        results [i] = "Case #"+str(i+1)+": Volunteer cheated!"
    elif (possible_cards == 1):
        results[i] =  "Case #"+str(i+1)+": "+str(correct_choice)
    else:
        results[i] =  "Case #"+str(i+1)+": Bad magician!"
    if (i != test_cases -1):
        results[i] = results[i]+"\n"

writeLinesToFile(results, output_path)