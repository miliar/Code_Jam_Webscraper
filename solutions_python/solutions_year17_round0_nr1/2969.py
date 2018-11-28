#!/usr/bin/python3
#SETTINGS:
SINGLE_INT_PER_ROW = False



nr_of_tasks = int(input())
result = ""

def validate(d):
    for i in range(0,len(d)):
        if not d[i]:
            return False
    return True



def task_calc(task_data):
    flipp_length = int(task_data[1])
    seq = [True if a=="+" else False for a in  task_data[0]]

    f_count= 0


    for i in range(0,len(seq)-flipp_length + 1):
        if not seq[i]:
            f_count+=1
            for j in range(0, flipp_length):
                seq[i+j] = not seq[i+j]


    if not validate(seq):
        return "IMPOSSIBLE"
    return str(f_count)





for task_index in range(0,nr_of_tasks):
    if SINGLE_INT_PER_ROW:
        inrow = int(input())
    else:
        inrow = [a for a in str(input()).split(" ")]
    result = task_calc(inrow)
    print("Case #{task}: {result}".format(task=task_index+1,
                                 result=str(result)))