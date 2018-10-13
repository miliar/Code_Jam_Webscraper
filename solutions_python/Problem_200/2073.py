def tidy (n):
    list = [int(i) for i in str(n)]
    if sorted(list) == list:
        return True
    else:
        return False

def findTidy (n):
    list = [str(i) for i in str(n)]
    if len(list) == 1 or tidy(n):
        return n
    while True:
        for i in range(len(list)-2,-1,-1):
            if list[i] > list[i+1]:
                list[i] = str(int(list[i])-1)
                for j in range(i+1, len(list)):
                    list[j] = '9'
        n = int(''.join(list))

        
        if tidy(n):
            return n

t = int(input())  # read a line with a single integer

for i in range(1, t + 1):
    n = int(input())
    answer = findTidy(n)
    print("Case #{}: {}".format(i, answer))