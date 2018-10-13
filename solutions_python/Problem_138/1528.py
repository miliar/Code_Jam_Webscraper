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

def optimal(list_n,list_k):
    list_n.sort()
    list_k.sort()
    n_wins = 0
    i = 0
    j = 0
    while(i < len(list_n) and j < len(list_k)):
        if list_k[j] > list_n[i]:
            n_wins -= 1
            i += 1
            j += 1
        else:
            j += 1
    return n_wins+len(list_n)

def deceitful(list_n,list_k):
    list_n.sort()
    list_k.sort()
    i = 0
    j = 0
    n_wins = 0
    while(i < len(list_n) and j < len(list_k)):
        if list_k[j] > list_n[i]:
            i += 1
        else:
            n_wins += 1
            i += 1
            j += 1
    return n_wins

def main_operation(input_list):
    cases = int(input_list[0][0])*3+1
    for i in range(1,cases,3):
        print "Case #%d: %d %d" % ((i-1)/3+1,deceitful(input_list[i+1],input_list[i+2]),optimal(input_list[i+1],input_list[i+2]))


test = file_tran(input_file)
main_operation(test)






