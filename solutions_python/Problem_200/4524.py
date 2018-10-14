def isTidyNumber(input): #checks if the given input is a tidy number
    for i in range(0, len(input)-1):
        if(int(input[i]) > int(input[i+1])):
            return False

    return True

file1 = open("B-small-attempt1.in","r").readlines()
file2 = []
for obj in file1:
    temp = obj.split()
    file2.append(temp[0])


for i in range(0, int(file2[0])):
    input_num = int(file2[i+1])
    while(isTidyNumber(str(input_num)) == False):
        input_num-= 1

    print("Case #" + str(i+1) + ": " + str(input_num))