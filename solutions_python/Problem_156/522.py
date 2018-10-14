import copy

def splitbiggest(lst):
    l = copy.deepcopy(lst)
    big = max(l)
    num = l.count(big)
    for x in range(0, num):
        l.remove(big)
        l.append(big//2)
        l.append(big - big//2)
    return l

def findleast(l):

    big = max(l)

    if big <= 3:
        return big

    num = l.count(big)

    trial = num + findleast(splitbiggest(l))

    if trial < big:
        return trial
    else:
        return big

def splitthree(num):
    if num <= 3:
        return 0
    ret = num // 3
    if num % 3 == 0:
        ret -= 1
    return ret

def total(l):
    return 3 + sum(list(map(splitthree, l)))

with open('B-small-attempt2.in') as f:
    stuff = f.readlines()

x = 2
case = 1

while x < len(stuff):
    lst = list(map(int, stuff[x].split()))
    print("Case #"+str(case)+": "+str(min(findleast(lst), total(lst))))
    x += 2
    case += 1
