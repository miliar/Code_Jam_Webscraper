#Problem A. Infinite House of Pancakes
__author__ = 'anna'
f = open('/Users/alevina/Mine/code_jam/code_jam_2017/a_sol_large', 'w')

tasks=[]
tasks_k=[]
N=0
def read_tasks():
    with open('/Users/alevina/Mine/code_jam/code_jam_2017/a_in_large','r') as f:
    #with open('/Users/alevina/Mine/Code_Jam_2014/c_small','r') as f:
        global T
        T=int(f.readline())
        k=1
        for line in f:
                lines=line.strip()
                linesl =  lines.split(' ')
                current_task = []
                for i in linesl[0]:
                    if i == '+':
                        current_task.append(0)
                    else:
                        current_task.append(1)

                tasks_k.append(int(linesl[1]))
                tasks.append(current_task)
                k += 1

def turn_pan(problem_list,index, k ):
    ret = problem_list;
    for i in range (index,index + k):
        if  problem_list[i] == 0:
            ret[i] = 1
        else:
            ret [i] = 0
    return ret


read_tasks();
#print tasks_k
#print tasks
#print T
#print sum(tasks[0])
for task_iterator in range(T):
    task = tasks[task_iterator]
    k = tasks_k[task_iterator]
    turn_num = 0
    num_not_sunny = sum(task)
    index = 0
#    print 'itarate:', len(task) - k +1
#    print 'len', len(task)
    while index < len(task) - k+1:
        if task[index] == 0:
            index += 1
        else:
            task = turn_pan(task, index, k)
            index += 1
            turn_num += 1
    solvable = 1;
    #for ind in range(index+1 , len(task)):
    if sum(task) != 0:
        solvable = 0
#    print 'solvable = ', solvable
    if  solvable == 1:
        f.write ("Case #" + str (task_iterator + 1) + ": " + str (turn_num) + "\n")
    else:
        f.write ("Case #" + str (task_iterator + 1) + ": IMPOSSIBLE"  + "\n")


