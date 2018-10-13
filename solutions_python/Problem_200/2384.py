from functools import reduce

num = int(input())  # read a line with a single integer
def intList (x):
    if x < 10:
        return [x]
    else:
        m = intList(x//10)
        m.append(x%10)
        return m

def listInt(l):
    k = [str(i) for i in l]
    s = reduce( (lambda x, y: x + y), k )
    ret = int(s)
    return ret

def ordering(l):
    max = 0
    j = 0
    size = len(l)
    if size <= 1:
        return l
    for i in range(size):
        if l[i] > max:
            max = l[i]
        elif l[i] < max:
            if (j == 0): j =i
            l[i] = 9
            max = 9
    if j != 0:
        k = l[0:j]
        m = intList(listInt(k)-1)
    else:
        m = l[0:j]
    k = ordering(m)
    k.extend(l[j:size])
    return k

for i in range(1, num + 1):
    x = int(input())
    print("Case #{}: {}".format(i, listInt(ordering(intList(x)))))
