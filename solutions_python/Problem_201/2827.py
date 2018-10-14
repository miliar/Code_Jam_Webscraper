#Problem B. Infinite House of Pancakes
__author__ = 'anna'
import bisect
import math
f = open('/Users/alevina/Mine/code_jam/code_jam_2017/c_sol_small1', 'w')

tasks=[]
tasks_hm=[]
N=0
def read_tasks():
    with open('/Users/alevina/Mine/code_jam/code_jam_2017/c_in1.in','r') as f:
   # with open ('/Users/alevina/Mine/code_jam/code_jam_2017/test', 'r') as f:#
    #with open('/Users/anna/Mine/Code_Jam_2014/c_small','r') as f:
        global T
        T=int(f.readline())
        k=1
        for line in f:
            lines=line.strip()
            tasks.append(map(int, lines.split(' ')))
            k += 1

def update_list(problem_list):
    NN = problem_list[-1]
    #print "NN = ", NN
    problem_list.pop()
    bisect.insort_left(problem_list,math.ceil((NN-1)/2.0))
    bisect.insort_left (problem_list, math.floor((NN-1) / 2.0))
    return problem_list


read_tasks();
for task_iterator in range(0,T):
# print task_iterator
    current_task=tasks[task_iterator]
# print current_task
    N = current_task[0]
    k = current_task[1]
#    print "N = ", N," k = ",k
    toilet_list = [N]
    for person in range(k-1):
        toilet_list = update_list(toilet_list);
   # print toilet_list
    last_person = toilet_list[-1] - 1
   # print "last_person ", last_person
    f.write("Case #"+ str(task_iterator+1)+": "+str(int(math.ceil(last_person/2.0)))+ " " +str(int(math.floor(last_person/2.0))) +"\n")
