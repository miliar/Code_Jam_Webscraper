t = int(input())

for i in range(1, t + 1):
    input_line = input()
    working_number = input_line
    for j in range(len(working_number)-1, 0, -1):

        if int(working_number[j]) < int(working_number[j-1]):
            working_number = working_number[0:j-1]+ str(int(working_number[j-1])-1) + "9"* (len(working_number)-j)


    if working_number[0] == "0":
        tidy_number = working_number[1:]
    else:
        tidy_number = working_number
    print("Case #{}: {}".format(i, tidy_number))
