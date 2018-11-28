from sys import stdin as fp

def max_tidy(n):
    while n>0:
        n = n-1
        if is_tidy(n):
            return n

        
def is_tidy(n):
    prev = 1
    for i in n:
        if i < prev:
            return False
        prev = i
    return True
    

def max_tidy_produce(num):
    n = [int(s) for s in str(num)]
    if is_tidy(n):
        return num
    for i in range(len(n)):
        cur = len(n) - i - 1
        if is_tidy(n[:cur]) and (i+1 >= len(n) or n[cur] - 1 >= n[cur-1]):
            lst = n[:cur] +  [n[cur] - 1] + [9]*i
            return int(''.join(str(el) for el in lst))

    
T = int(fp.readline())
for i, n in enumerate(fp):
    print("Case #{}: {}".format(i+1, max_tidy_produce(int(n))))

