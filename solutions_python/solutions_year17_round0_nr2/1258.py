from itertools import *


T = int(input())


def convert(table):
    prev = 0
    for i, a in enumerate(table):
        if prev > a:
            arr[i-1] = prev-1
            while i < len(table):
                table[i] = 9
                i += 1
            return True
        prev = a
    return False


for i in range(T):

    arr = [int(i) for i in input()]

    loop = True
    while loop:
        loop = convert(arr)
        
    
    answer = "".join(map(str, dropwhile(lambda x: x == 0, arr)))

    print(f"Case #{i+1}: {answer}")
