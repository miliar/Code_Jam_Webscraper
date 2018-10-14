__author__ = 'iToR'

file_name = "A-small-attempt0.in"

def findMutual(array1,array2):
    mutual = []
    for item in array1:
        if item in array2:
            mutual.append(item)
    return mutual

def generateOutput(guessCard, case):
    ans = ""
    if len(guessCard) == 0:
       ans = "Volunteer cheated!"
    elif len(guessCard) == 1:
        ans = guessCard[0]
    else:
        ans = "Bad magician!"
    ans_file = open("answer.txt", "a")
    ans_file.write("Case #" + str(case) + ": ")
    ans_file.write(ans + "\n")

f = open(file_name)

input_num = int(f.readline())

for i in range(1,input_num+1):
    first_guess_row = int(f.readline())
    check_row = ""
    for ref_index in range(1,5):
        if ref_index == first_guess_row:
            check_row = f.readline()
        else:
            f.readline()
    first_guess_array = check_row.split()
    second_guess_row = int(f.readline())
    check_row = ""
    for ref_index in range(1,5):
        if ref_index == second_guess_row:
            check_row = f.readline()
        else:
            f.readline()
    second_guess_array = check_row.split()
    mutual_card = findMutual(first_guess_array,second_guess_array)
    generateOutput(mutual_card,i)