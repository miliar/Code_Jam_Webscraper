import numpy as np

def get_tidy_new(n):
    digits = [int(i) for i in list(str(n))]
    for j in range(len(digits)-2,-1,-1):
        k = j+1
        if((j==0) and (digits[j]==1)):
            if(digits[j]>digits[k]):
                digits = [int(i) for i in np.ones((len(digits)-1))*9]
        else:
            if(digits[j]>digits[k]):
                digits[j] = digits[j] - 1
                for i in range(k,len(digits)):
                    digits[i] = 9
    return int("".join([str(i) for i in digits]))


t = int(input())

for i in range(1,t+1):
    print("Case #%d:" % i,get_tidy_new(int(input())))

