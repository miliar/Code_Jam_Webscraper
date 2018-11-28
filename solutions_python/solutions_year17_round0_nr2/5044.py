
lst_problemInput = []
lst_problemOutput = []

def IsNumberTidy(number_to_check):
    highest_number = 0
    tidy_found = True
    for j in str(number_to_check):
        if int(j) < highest_number:
            # number is not tidy!
            tidy_found = False
            break
        else:
            highest_number = int(j)
    return tidy_found

with open('B-small-attempt0.in') as f:
    lst_problemInput = f.readlines()

num_testcases = int(lst_problemInput[0])

for i in range(num_testcases):
    number_to_check = int(lst_problemInput[i + 1])
    # number_to_check = number_to_check - i
    #is this number tidy?
    if number_to_check < 10:
        lst_problemOutput.append("Case #" + str(i+1) + ": " + str(number_to_check))
    else:
        tidy_found = IsNumberTidy(number_to_check)
        if tidy_found == True:
            lst_problemOutput.append("Case #" + str(i + 1) + ": " + str(number_to_check))
        while tidy_found == False:
            number_to_check = number_to_check - 1
            tidy_found = IsNumberTidy(number_to_check)
            if (tidy_found == True):
                lst_problemOutput.append("Case #" + str(i + 1) + ": " + str(number_to_check))


thefile = open('b_output.txt', 'w')
for item in lst_problemOutput:
  thefile.write("%s\n" % item)
thefile.close()

