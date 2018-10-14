import sys
import math

testnum = int(input().strip())

for cnum in range(testnum):
    n, p = input().strip().split(' ')
    n = int(n)
    p = int(p)
    step = math.floor(math.log2(p))
    


    numset = []
    temp_numset = []
    numset.append(n)
    if step > 0:
        for s in range(step):
            for num in numset:
                if num % 2 == 0:
                    temp_numset.append(int(num/2)-1)
                    temp_numset.append(int(num/2))
                else:
                    temp_numset.append(int((num-1)/2))
                    temp_numset.append(int((num-1)/2))
            numset = temp_numset
            temp_numset = []
        numset.sort(reverse=True)

        p_last = p - math.pow(2, math.floor(math.log2(p)))
        p_last = int(p_last)
        num_last = numset[p_last]
        
        if num_last % 2 == 0:
            min_lr = num_last/2 - 1
            max_lr = num_last/2
        else:
            min_lr = math.floor(num_last/2)
            max_lr = min_lr


    else:
        if n % 2 == 0:
            min_lr = n/2 - 1
            max_lr = n/2
        else:
            min_lr = math.floor(n/2)
            max_lr = min_lr
    
    min_lr = int(min_lr)
    max_lr = int(max_lr)

    print("Case #"+str(cnum+1)+": "+str(max_lr)+" "+str(min_lr))