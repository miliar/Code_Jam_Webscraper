import fileinput
from math import floor
file = fileinput.input()
num_case = int(file.readline())
for ith_case in range(num_case):
    C,F,X = tuple(map(float, file.readline().strip().split()))
    n_farm = floor(X/C - 2/F)
    n_farm = 0 if n_farm < 0 else n_farm
    time = 0
    for i in range(n_farm):
        time += C/(2+i*F)
    time += X/(2+n_farm*F)
    print("Case #{}: {}".format(ith_case+1,time))
