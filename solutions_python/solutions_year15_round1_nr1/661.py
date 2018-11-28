__author__ = 'anna'
#Problem A. Mushroom Monster

f = open('/Users/anna/Mine/code_jam/code_jam_2015/1A/a_sol_large', 'w')

tasks=[]
tasks_hm=[]
N=0
def read_tasks():
    with open('/Users/anna/Mine/code_jam/code_jam_2015/1A/a.in','r') as f:
    #with open('/Users/anna/Mine/Code_Jam_2014/c_small','r') as f:
        global T
        T=int(f.readline())
        k=1
        for line in f:
            if k%2==0:
                lines=line.strip()
                tasks.append(map(int, lines.split(' ')))
            else:
                lines=line.strip()
                tasks_hm.append(int(lines))
            k += 1

read_tasks()
#print tasks
for t in range(T):
    #m=tasks_hm(t)
    minus_list=[]
   # print "task nummer", t
   # print tasks[t]
   # print "task length", (len(tasks[t])-1)
   # print tasks[t][(len(tasks[t])-1)]

    for ii in range(1, (len(tasks[t]))):
     #   print (tasks[t][ii-1]-tasks[t][ii])
        if ((tasks[t][ii-1]-tasks[t][ii])>0):
            minus_list.append(tasks[t][ii-1]-tasks[t][ii])
   # print minus_list
    if not minus_list:
        Way1=0
        Way2=0
    else:
        Way1=sum(minus_list)
        MaxDiff=max(minus_list)
       # print "MaxDiff", MaxDiff
        Way2=0
        #tasks.pop()
        for iter in range(len(tasks[t])-1):
        #    print "iter=",iter, " tasks[iter]=", tasks[t][iter]
            Way2+=min(MaxDiff,tasks[t][iter])

    f.write("Case #"+ str(t+1) + ": " + str(Way1) + " " + str(Way2) + "\n")


