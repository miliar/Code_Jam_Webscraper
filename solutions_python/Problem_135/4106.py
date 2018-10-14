def solve(case_no,lst):
    guessed_row_number_one = int(lst[0])
    guessed_row_number_two = int(lst[5])
    guessed_row_one = lst[guessed_row_number_one].split(' ')
    print guessed_row_one
    guessed_row_two = lst[5+guessed_row_number_two].split(' ')
    print guessed_row_two
    common_number_found = []
    f = open('output.txt','a')
    for item in guessed_row_one:
        if item in guessed_row_two:
            common_number_found.append(item)
    if len(common_number_found) == 1:
        f.write("Case #"+str(case_no+1)+":"+' '+common_number_found[0]+'\n')
    elif len(common_number_found) > 1:
        f.write("Case #"+str(case_no+1)+":"+' '+'Bad magician!\n')
    else:
        f.write("Case #"+str(case_no+1)+":"+' '+'Volunteer cheated!\n')

f = open('A-small-attempt2014.in')
lines = f.readlines()
#print lines
cleaned_lines = []
number_of_test_cases = int(lines[0].strip())
for item in lines[1:]:
    cleaned_lines.append(item.strip())
#print cleaned_lines,number_of_test_cases
for test_case in range(number_of_test_cases):
    begin_idx = 10 * test_case
    #print cleaned_lines[begin_idx:begin_idx+10]
    solve(test_case,cleaned_lines[begin_idx:begin_idx+10])

