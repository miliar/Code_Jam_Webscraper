'''
Created on Apr 11, 2015

@author: Federico
'''
output_file = open('output_file.out', 'wb')

with open('A-large.in', 'rb') as stream:
    for index, each_line in enumerate(stream):
        if index == 0:
            number_test = int(each_line.strip())
        else:
            s_max, s_number = each_line.strip().split()
            s_max = int(s_max)
            s_number = map(int, list(s_number))
            
            if s_max == 0:
                result_string = 'Case #{}: 0'. format(index)
            else:
                current_standing = s_number[0]
                extra_people = 0
                
                for level_k in range(1, s_max + 1):
                    if level_k <= current_standing:
                        current_standing += s_number[level_k]
                    else:
                        difference = level_k - current_standing
                        extra_people += difference
                        current_standing += difference
                        current_standing += s_number[level_k]
                        
                result_string = 'Case #{}: {}'. format(index, extra_people)
                
            print result_string
            output_file.write(result_string + '\n')