#from mpmath import *
#from bigfloat import *
def add_farm(farm_time, curr_base, F, X):
    time = farm_time + X/(curr_base+F)
    return time
f = open('B-large.in', 'r')
num=int(f.readline())
output=open('result','w')
case=0
base=2.0
while num!=0:
    num-=1
    case+=1
    row = [float(x) for x in f.readline().split()]
    C=row[0]
    F=row[1]
    X=row[2]
    best_result = X/base
    current_base = base
    addiional_time = 0.0
    while True:
        farm_time = C/current_base
        time_curr = add_farm(farm_time, current_base, F, X)
        if (time_curr+addiional_time) < best_result:
            best_result = time_curr+addiional_time
            addiional_time += farm_time
            current_base += F
        else:
            break
        
    print('Case #'+str(case)+': '+str(best_result))
    output.write('Case #'+str(case)+': '+str(best_result)+'\n')
output.close()
