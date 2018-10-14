import Queue as Q
import time
import math
fin = open('./C-large.in','r')
fout = open('./outputC.txt','w')

t = int(fin.readline())
for i in range(0,t):
    
    n,k = fin.readline().split()
    n = int(n)
    k = int(k)
    d = math.floor(math.log(k+1,2))
    remain_person = k - 2**d + 1

    if remain_person == 0:
        d = d - 1
        remain_person = k - 2**d + 1
    
    remain_space = n - 2**d + 1
    avg_space = remain_space/2**d
    min_space = math.floor(avg_space)
    max_space = math.ceil(avg_space)
    no_min = (min_space+1)*2**d-remain_space
    no_max = 2**d -no_min
    #print remain_person
    #print no_min,min_space,'-',no_max,min_space+1
    #print remain_person,no_max
    if remain_person == 0:
        space_left = int(min_space)
        space_right = int(max_space)
    else:
        if remain_person <= no_max:
            space = max_space-1
        else:
            space = min_space - 1
        space_left = int(space/2)
        space_right = int(space - space_left)
    print space_right,space_left
    fout.write('Case #{}: {} {}\n'.format(i+1,max(space_left,space_right),min(space_left,space_right)))

fin.close()
fout.close()
