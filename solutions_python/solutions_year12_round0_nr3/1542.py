def isRecycled(int1, int2):
    str1 = str(int1)
    str2 = str(int2)
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        part1 = str1[:i]
        part2 = str1[i:]
        total = part2 + part1
        if total == str2:
            return True
    return False


a_file = open('C-small-attempt0.in')
numcases = int(a_file.readline())

for k in range(numcases):
    
    param = a_file.readline()
    params = param.split()
    start = int(params[0])
    end = int(params[1])
    counter = 0
    for i in range(start, end + 1):
        for j in range(i + 1, end+1):
            if isRecycled(i, j):
                counter += 1
     
    
    print("Case #" + str(k + 1) + ":", counter)






    
