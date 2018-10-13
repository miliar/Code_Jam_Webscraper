def checkLists(first, second):
    count = 0
    match = 0
    for num in first:
        if num in second:
            count += 1
            match = num
    if count == 1:
        return match
    if count == 0:
        return 0
    return -1

f = open('A-small-attempt0.in','r')
g = open('A-small.out','w')
a = f.read()
b = a.split('\n')

cases = (int)(b[0])

for i in range(0,cases):
    first = (int)(b[i*10+1])
    nums = b[i*10 + 1 + first].split(" ")
    second = (int)(b[i*10 + 6])
    secNums = b[i*10 + 6 + second].split(" ")

    matching = checkLists(nums, secNums)
    
    if (matching == -1):
        g.write("Case #"+(str)(i+1)+": Bad magician!\n")
    elif (matching == 0):
        g.write("Case #"+(str)(i+1)+": Volunteer cheated!\n")
    else:
        g.write("Case #"+(str)(i+1)+": "+(str)(matching)+"\n")

f.close()
g.close()
