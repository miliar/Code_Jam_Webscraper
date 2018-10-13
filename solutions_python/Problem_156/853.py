import numpy as np
f = open('./B-small-attempt0.in')
lines = f.readlines()
f.close()

case = lines[0]
case=case.strip('\n')

f = open('./output.txt','wb')

def cal_time2(array):
    split = 1;
    min_time = 0
    for j in range(0, len(array)):
        min_time += array[j] - 1;
    
    for split_max in range(2, array[-1]-1):
        time = 0
        for j in range(0, len(array)):
            if (array[j] % split_max == 0):
                time += array[j] / split_max - 1
            else:
                time += array[j] / split_max
        time += split_max
        if time < min_time:
            min_time = time
    if (min_time > array[-1]):
        min_time = array[-1]
    return min_time

i = 2
while (i <= 200) :
    person = lines[i]
    person =person.strip('\n')
    strs = person.split(' ')
    n = [ int( strs ) for strs in strs if strs ]
    sort_n = sorted(n, key=int) 
    
    print sort_n
    if sort_n[len(sort_n) - 1] <= 3:
        s = "Case #" + str(i/2) + ": "+str(sort_n[len(sort_n) - 1])+"\n"
        f.write(s)
        i += 2
        continue
        
    maxx = sort_n[-1]
    time = cal_time2(sort_n)
    
    if time > maxx:
        time = maxx
    s = "Case #" + str(i/2) + ": "+str(time)+"\n"
    f.write(s)
    i += 2
f.close()


