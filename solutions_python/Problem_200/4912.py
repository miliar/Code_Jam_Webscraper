import itertools

def isTidy(lst):
    for i in range(len(lst) - 1):
        if lst[i]>lst[i+1]:
            return False
    return True

def tidiest(count):
    count = str(count)
    if len(count) == 1:
        return int(count)
    else:
        for i in range(int(count), 9, -1):
            
            lst = [int(j) for j in str(i)]
            if isTidy(lst):
                return i

t = int(input())
for i in range(1, t+1):
    n = input()
    print("Case #{}: {}".format(i, tidiest(n)))

