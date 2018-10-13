t = int(input())

def reduce(n):
    ctr = i = 0
    while(ctr == 0):
        temp = [int(x) for x in str(n)]
        if check(temp):
            return n
            ctr = 1
        else:
            n -= 1
        if ctr == 1:
            break
        i += 1

def check(lst):
    for i in range(len(lst)):
        try:
            if lst[i] < lst[i+1] or lst[i] == lst[i+1]:
                continue
            else:
                return 0
                break
        except IndexError:
            break
    return 1

for i in range(t):
    n = int(input())
    temp = [int(x) for x in str(n)]
    if len(temp) == 1:
        print("Case #{0}: {1}".format(i+1, n))
        continue
    elif all(x == temp[0] for x in temp):
        print("Case #{0}: {1}".format(i+1, n))
        continue
    else:
        print("Case #{0}: {1}".format(i+1, reduce(n)))


