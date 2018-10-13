from sys import argv

script , input_file = argv

#file input

def file_tran(input_file):
    list = []
    f = open(input_file)
    for line in f.readlines():
        line = line.strip('\n')
        line = line.split(' ')
        line_1 = []
        for i in line:
            line_1.append(int(i))
        list.append(line_1)
    return list

def com(list1,list2):
    flag = 0
    num = 0
    for val in list1:
        if val in list2:
            flag += 1
            num = val
    if flag == 1:
        return num*10
    else:
        return flag

#main manipulation of the input
def magic(list_input):
    cases = list_input[0][0]*10+1
    count = 1
    for i in range(1,cases,10):
        line_1 = list_input[i][0]
        tmp_1 = list_input[i+line_1]
        line_2 = list_input[i+5][0]
        tmp_2 = list_input[i+5+line_2]
        flag = com(tmp_1,tmp_2)
        if flag == 0:
            print "Case #%d: Volunteer cheated!" % count
        elif flag >= 10:
            print "Case #%d: %d" % (count,flag/10)
        else:
            print "Case #%d: Bad magician!" % count
        count += 1


test = file_tran(input_file)            
magic(test)



