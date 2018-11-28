def main():
    for case in range(input()):
        digit_count_list = [0 for i in range(10)]
        meaning_digit_count = 0
        original_number_string = raw_input()
        for charactor in original_number_string:
            if charactor != '0':
                digit_count_list[int(charactor)] += 1
                meaning_digit_count += 1
        stack = []
        count_list = digit_count_list[:]
        for index in range(len(original_number_string)):
            for digit_index in range(9, int(original_number_string[index]), -1):
                if digit_index == 0 or count_list[digit_index] > 0:
                    temp_count_list = count_list[:]
                    if digit_index > 0:
                        temp_count_list[digit_index] -= 1
                    stack.append((index, temp_count_list, original_number_string[:index] + str(digit_index)))
#                    print index, temp_count_list, original_number_string[:index] + str(digit_index)
            if int(original_number_string[index]) > 0:
                count_list[int(original_number_string[index])] -= 1
        next_number_string = ""
        while stack:
            index, count, prefix = stack.pop()
            if index != len(original_number_string) - 1:
#                print index, count, prefix
                for digit_index in range(9, -1, -1):
#                    print digit_index, int(original_number_string[index]) - 1
                    if digit_index == 0 or count[digit_index] > 0:
                        temp_count_list = count[:]
                        if digit_index > 0:
                            temp_count_list[digit_index] -= 1
                        stack.append((index + 1, temp_count_list, prefix + str(digit_index)))
#                        print index + 1, temp_count_list, prefix + str(digit_index)
            else:
                if not any(count) and prefix != original_number_string:
                    next_number_string = prefix
                    break
        count_list = digit_count_list[:]
        if not next_number_string:
            for index in range(10):
                if count_list[index] > 0:
                    count_list[index] -= 1
                    next_number_string = str(index)
                    break
            for i in range(len(original_number_string) + 1 - meaning_digit_count):
                next_number_string += '0'
            for index in range(10):
                while count_list[index] > 0:
                    count_list[index] -= 1
                    next_number_string += str(index)
#                print next_number_string, count_list
        print "Case #%d: %s" % (case + 1, next_number_string)
        
main()
