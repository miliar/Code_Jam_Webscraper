'''
Created on 2010-05-08

@author: lawford
'''

import random
    
def attempt2(groups, slots):
#    print("groups="+str(groups)+", slots="+str(slots))
    
    slots = min(slots, sum(groups))
    
    dynamic = []
    cycle = []

    extended_groups = groups + groups
    
    targets = set()
    for i in range(0,len(groups)):
        filled = 0
        j = i
        while filled+extended_groups[j] <= slots:
            filled = filled + extended_groups[j]
            j = j+1
        j = j % len(groups)
        piece = (False, i, [(filled, j)])
        dynamic.append(piece)
        targets.add(j)
        cycle.append(False)

    while (len(targets) > 0):
        new_targets = set()
        for dyna in dynamic:
            my_id = dyna[1]
            if not (my_id in targets):
                continue
            dyn = dyna[2]
    #        head = dyn[0]
    #        tail = dynamic[head[1]][rep]
            tail = dyn[-1]
            if (tail[1] == my_id):
                continue        
            head = dynamic[tail[1]][2][0]
            dyn.append((head[0]+tail[0], head[1]))
            new_targets.add(head[1])
        targets = new_targets
    
    return dynamic
        

def solution(groups, slots, runs):
    dynamic = attempt2(groups, slots)
    
    income = 0
    point = 0
    while runs > 0:
        lenx = len(dynamic[point][2])
        step = min(runs, lenx)
        block = dynamic[point][2][step-1]
        my_id = dynamic[point][1]
        if (my_id == block[1]):
            step_mult = runs/lenx
            income = income + block[0]*step_mult
            step = step_mult*lenx
        else:
            income = income + block[0]
        point = block[1]
        runs = runs - step

#    for n in dynamic:
#        print(n)

    return income
if __name__ == '__main__':
#    groups = [1,4,2,1]
#    groups = [random.randint(1,5) for i in range(1,10)]
#    slots = 6
#    runs = 1000000
#    
#    income = solution(groups, slots, runs)
    
#    print("groups is "+str(groups))
#    print("income is "+str(income))

    data = []
    f = open("/raid/downloads/firefox/C-large.in", "r")
    line = f.readline()
    while line != '':
        line1 = f.readline()
        if line1 == '':
            break
        line = f.readline()
        if line == '':
            break
        data.append([[int(n) for n in line1.split()], [int(n) for n in line.split()]])
        

    fout = open("/tmp/C-large.out", "w")
    i = 1
    for info in data:
        fout.write("Case #"+str(i)+": "+str(solution(info[1], info[0][1], info[0][0]))+"\n")
        i = i +1
    
    fout.close()
    f.close()
    