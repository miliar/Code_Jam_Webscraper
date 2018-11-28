import sys
import string

input_list = []
output_list = []

def HandleInputTestCase():
    global input_list

    input_file = open(sys.argv[1], 'r')

    case_num = string.atoi(input_file.readline())

    for case_index in range(case_num):
        temp = [x for x in input_file.readline().split(' ')]
        case = {}

        index = 0
        case['combinelist_num'] = string.atoi(temp[index])
        index += 1
        case['combinelist'] = []
        for i in range(case['combinelist_num']):
            case['combinelist'].append(list(temp[index]))
            index += 1

        case['opposelist_num'] = string.atoi(temp[index])
        index += 1
        case['opposelist'] = []
        for i in range(case['opposelist_num']):
            case['opposelist'].append(list(temp[index]))
            index += 1
                
        case['elementlist_num'] = string.atoi(temp[index])
        index += 1
        case['elementlist'] = list(temp[index][:-1])

        input_list.append(case)

    input_file.close()
    
def HandleOutputTestCase():
    global output_list
    output_file = open('result_' + sys.argv[1], 'w')

    for index in range(len(output_list)):
        output_file.write('Case #' + str(index+1) + ': [')
        for i in range(len(output_list[index])):
            output_file.write(output_list[index][i])
            if i != len(output_list[index])-1:
                output_file.write(', ')
        output_file.write(']\n')

    output_file.close()

def Magicka(case_dict):
#    print 'case = ', case_dict

    temp_list = []
    for element in case_dict['elementlist']:
        temp_list.append(element)
#        print 'temp = ', temp_list
        
        if len(temp_list) <= 1:
            continue

        # Combine
#        print 'com1=', temp_list[-2:]
        for combine in case_dict['combinelist']:
#            print 'com2=', combine[:2]
            if (combine[0] == combine[1] and combine[:2] == temp_list[-2:]) or \
               (combine[0] != combine[1] and combine[0] in temp_list[-2:] and combine[1] in temp_list[-2:]):
                temp_list = temp_list[:-2] + combine[-1:]
#                print 'combine = ', temp_list

        # Oppose
        for oppose in case_dict['opposelist']:
            if oppose[0] in temp_list and oppose[1] in temp_list:
                temp_list = []
#                print 'oppose = ', temp_list
            
#    print 'result = ', temp_list
    return temp_list


HandleInputTestCase()
#print '-'*30
for case in input_list:
    output_list.append( Magicka(case) )
#    print '-'*30
HandleOutputTestCase()
