'''
Google Code Jam 2009
Round 1B
B.

@author: Samuel Spiza
'''

#fileName = "B-practice.in"
#fileName = "B-small-attempt2.in"
fileName = "B-large.in"
file = open(fileName, "r")

def findNext(K):
    arr = list(str(K))
    j = len(arr) - 2
    while 0 <= j:
        temp = arr[j + 1:]
        temp.sort()
        blah = -1
        while 0 < len(temp) and temp[-1] > arr[j]:
                blah = temp.pop(-1)
        if blah != -1:
            newtemp = arr[j + 1:]
            newtemp.remove(blah)
            newtemp.append(arr[j])
            newtemp.sort()
            newarr = arr[:j] + [blah] + newtemp
            return "".join([str(x) for x in newarr])
        j = j -1
    arr.sort()
    arr[1:1] = [0]
    arr = [int(x) for x in arr]
    small = 10
    for t in arr:
        if t != 0 and t < small:
            small = t
    print small
    print arr
    arr.remove(small)
    arr[0:0] = [small]
    return "".join([str(x) for x in arr])
    
        

i = -1
j = 0
string = ""

for line in file:
    if i == -1:
        T = int(line.strip())
        i = 1
    elif i == 0:
        j = j + 1
        i = 1
        K = int(line.strip())
        string = string + "Case #" + str(j) + ": " + str(findNext(K)) + "\n"
    i = i - 1


file.close()





    
file = open(fileName.rsplit(".", 1)[0] + ".out", "w")
file.write(string.strip())
file.close()
