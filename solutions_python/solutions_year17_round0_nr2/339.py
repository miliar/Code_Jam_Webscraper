def checktidy(number):
    number = str(number)
    if len(number) == 1:
        return True
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            return False
    return True

file = open("B-large.in", "r")
infile = [i for i in file.readlines()]
test_cases = int(infile[0])
input_cases = []
newfile = open("GCI_2.txt", "w")
for j in range(1, test_cases + 1):          #first element is number of test cases (just checking that)
    input_cases.append(infile[j])
for j in range(len(input_cases)):
    curr_number = input_cases[j].strip()
    if not checktidy(curr_number):
        for i in range(len(curr_number) - 1, 0, -1):
            if curr_number[i] < curr_number[i - 1]:
                curr_number = curr_number[:i - 1] + str(int(curr_number[i - 1]) - 1) + "9" * (len(curr_number) - i)
        curr_number = int(curr_number)          #get rid of leading zeroes
    if not checktidy(curr_number):
        print ("False")
    else:
        print ("True")
    newfile.write("Case #{0}: {1}\n".format(j + 1, curr_number))
newfile.close()
