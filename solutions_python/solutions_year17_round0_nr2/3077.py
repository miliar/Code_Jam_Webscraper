import os

case_num = 1

def num_conv(a):
    a_string = str(a)
    a_final_string = ''
    a_list = []
    for i in range(0, len(a_string)):
        a_list.append(int(a_string[i]))
    for j in range(0, len(a_list)-1):
        if a_list[j] > a_list[j+1]:
            a_list[j] -= 1
            for k in range(j+1, len(a_list)):
                a_list[k] = 9
            for t in range(len(a_list)-1, 0,-1):
                if a_list[t] < a_list[t-1]:
                    a_list[t] = 9
                    a_list[t-1] = a_list[t-1] - 1
    if a_list[0] == 0:
        a_list = a_list[1:]
    for l in range(0, len(a_list)):
        a_final_string = a_final_string + str(a_list[l])
    return int(a_final_string)

with open('B-large.in', 'rb') as text_file:
    t = text_file.readline().strip('\r\n')
    for line in text_file:
        line = line.strip('\r\n')
        print 'Case #%s: %s' % (case_num, num_conv(line))
        case_num += 1



