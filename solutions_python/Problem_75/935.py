def changeletter(change_dict, letters):
    if letters[-2:] in change_dict:
        letter_to_change = letters[-2:]
        letters = letters[:-2]
        letters += change_dict[letter_to_change]
    if letters[-2:][::-1] in change_dict:
        letter_to_change = letters[-2:][::-1]
        letters = letters[:-2]
        letters += change_dict[letter_to_change]
    return letters

def removeletter(remove_list, letters):
    for remove in remove_list:
        if remove[0] in letters:
            if remove[1] in letters:
                    letters = ""
                    break
    return letters

def invokeletters(change_dict,remove_list,letters):
    new_letter = ''
    for letter in letters:
        new_letter += letter
        if not len(new_letter) == 1:
            if not change_dict == '':
                new_letter = changeletter(change_dict, new_letter)
            if not remove_list == '':
                new_letter = removeletter(remove_list, new_letter)
    return new_letter

in_file = open("in")
out_file = open("out","w")
test_cases = int(in_file.readline())
for test in range(test_cases):
    test_line = in_file.readline()
    test_info = test_line.split(" ")
    if not int(test_info[0]) == 0:
        change_dict = dict()
        for let in range(int(test_info[0])):
            change_dict[test_info[let+1][:2]] = test_info[let+1][2:]
    else:
        change_dict = ''
    test_info = test_info[int(test_info[0])+1:]

    if not int(test_info[0]) == 0:
        remove_list = list()
        for let in range(int(test_info[0])):
            remove_list.append(test_info[let+1])
    else:
        remove_list = ''
    test_info = test_info[int(test_info[0])+1:]

    new_letters = invokeletters(change_dict,remove_list,test_info[-1][:-1])


    split_letters = ''
    for letters in new_letters:
        split_letters += letters
        split_letters += ", "
    split_letters = split_letters[:-2]
    
    out_file.write("Case #" + str(test + 1) + ": [" + split_letters + "]\n")
out_file.close()
in_file.close()

     
    
    
    
