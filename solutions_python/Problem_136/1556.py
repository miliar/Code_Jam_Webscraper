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
            line_1.append(float(i))
        list.append(line_1)
    return list

#cc operation

def cookie(c,f,x):
    time_old = x/2
    time_new = c/2+x/(f+2)
    count = 1
    while(time_old > time_new):
        time_old = time_new
        time_new = time_new - x/(f*count+2) + c/(2+count*f) + x/(f*(count+1)+2)
        count += 1
    return time_old


def get_all_cookies(input_list):
    cases = int(input_list[0][0])
    count = 1
    for i in range(1,cases+1):
        print "Case #%d: %f" %(count,cookie(input_list[i][0],input_list[i][1],input_list[i][2]))
        count += 1

test = file_tran(input_file)
get_all_cookies(test)
