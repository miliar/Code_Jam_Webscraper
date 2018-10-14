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
        case['item_num'] = string.atoi(temp[0])
        case['btn_order'] = []
        for index in range(1, len(temp), 2):
            case['btn_order'].append([temp[index], string.atoi(temp[index+1])])
        input_list.append(case)
##        print 'case = ', case_index
##        print 'data = ', case['btn_order']
##        print '\n'

    input_file.close()
    
def HandleOutputTestCase():
    global output_list
    output_file = open('result_' + sys.argv[1], 'w')

    for index in range(len(output_list)):
        output_file.write('Case #' + str(index+1) + ': ')
        output_file.write(str(output_list[index]))
        output_file.write('\n')

    output_file.close()

def BotTrust(button_list):
    total_sec = 0
    cur_pos = {'O':1, 'B':1} # current robot position
    acc_sec = 0
    acc_robot = button_list[0][0]
    for btn in button_list:
#        print 'seq = ', btn
        pos_diff = abs(btn[1] - cur_pos[btn[0]])
#        print 'pos_diff = ', pos_diff
#        print 'acc_robot(before) = ', acc_robot
#        print 'acc_sec(before) = ', acc_sec

        if btn[0] == acc_robot:
            total_sec += pos_diff + 1
            acc_sec += pos_diff + 1
        else:
            temp = pos_diff - acc_sec
            if temp > 0:
                total_sec += temp + 1
                acc_sec = temp + 1
            else:
                total_sec += 1
                acc_sec = 1
            acc_robot = btn[0] # change accumelated robot

        cur_pos[btn[0]] = btn[1]
 #       print 'acc_robot(after) = ', acc_robot
 #       print 'acc_sec(after) = ', acc_sec
 #       print 'total_sec = ', total_sec
 #       print '\n'

    return total_sec


HandleInputTestCase()
#print '-'*30
for case in input_list:
    output_list.append( BotTrust(case['btn_order']) )
#    print '-'*30
HandleOutputTestCase()
