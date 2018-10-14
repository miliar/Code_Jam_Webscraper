import math

t = int(raw_input())
magic = lambda nums: int(''.join(str(i) for i in nums))
for i in xrange(1, t + 1):
    s_string_list = list(raw_input())
    contains_zero = False
    contains_last_zero = False
    s_int_list = map(int, s_string_list)
    
    for digits in range(0,len(s_string_list)):
        if s_string_list[digits] == '0':
            contains_zero = True
    
    if contains_zero == True and s_int_list[0] == 1:
        contains_last_zero = True

    if contains_last_zero == True:
        s_new_list = []
        times_to_iterate = len(s_string_list)
        while times_to_iterate > 1:
            s_new_list.append(9)
            times_to_iterate = times_to_iterate - 1 
        print "Case #%d: %d" % (i, magic(s_new_list))

    if contains_last_zero == False and contains_zero == True:
        last_ascending = 0
        last_ascending_matching = 0
        largest = 0
        for numbers in s_int_list:
            if numbers >= largest:
                largest = numbers
                last_ascending += 1
                continue
            else:
                break
        for numbers in range(last_ascending - 1, 0, -1):
            if s_int_list[numbers] == s_int_list[numbers - 1]:
                last_ascending_matching += 1
        nines_remaining = len(s_string_list) - last_ascending + 1
        s_new_list = []
        for numbers in range(0, last_ascending):
            s_new_list.append(s_int_list[numbers])
        if last_ascending < len(s_string_list):
            s_new_list[last_ascending - 1] -= 1
        if last_ascending_matching > 0 and last_ascending < len(s_string_list):
            if last_ascending_matching > 0:
                s_new_list[last_ascending - last_ascending_matching - 1] -= 1
                s_new_list.pop()
                nines_remaining += last_ascending_matching
        while nines_remaining > 1:
            s_new_list.append(9)
            nines_remaining -= 1
        print "Case #%d: %d" % (i, magic(s_new_list))

    if contains_zero == False:
        last_ascending = 0
        last_ascending_matching = 0
        largest = 0
        for numbers in s_int_list:
            if numbers >= largest:
                largest = numbers
                last_ascending += 1
                continue
            else:
                break
        for numbers in range(last_ascending - 1, 0, -1):
            if s_int_list[numbers] == s_int_list[numbers - 1]:
                last_ascending_matching += 1
        nines_remaining = len(s_string_list) - last_ascending + 1
        s_new_list = []
        for numbers in range(0, last_ascending):
            s_new_list.append(s_int_list[numbers])
        if last_ascending < len(s_string_list):
            s_new_list[last_ascending - 1] -= 1
        if last_ascending_matching > 0 and last_ascending < len(s_string_list):
            if last_ascending_matching > 0:
                s_new_list[last_ascending - last_ascending_matching - 1] -= 1
                s_new_list.pop()
                nines_remaining += last_ascending_matching
        while nines_remaining > 1:
            s_new_list.append(9)
            nines_remaining -= 1
        print "Case #%d: %d" % (i, magic(s_new_list))