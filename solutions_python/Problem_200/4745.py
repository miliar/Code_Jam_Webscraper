#MY_PROGRAM < sample.txt
#MY_PROGRAM < small_input.txt > small_output.txt
#MY_PROGRAM < large_input.txt > large_output.txt

def checkiftidy(number):
    checkpreposnum = int(str(number)[0])
    for posnumber in str(number)[1:]:
        #print(checkpreposnum, posnumber)
        if int(checkpreposnum) > int(posnumber):
            return False
        checkpreposnum = posnumber
    return True

t = int(input())
for i in range(1, t + 1):
    number = int(input())
    while not checkiftidy(number):
        number -= 1
    print("Case #{}: {} ".format(i, number))