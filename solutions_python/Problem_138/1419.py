file1 = open('input.txt')
file2 = open('output.txt','w')
a = int(file1.readline())
x = 1
while (a > 0):
    b = int(file1.readline())
    c = file1.readline()
    d = file1.readline()
    sumit = c.split()
    amit = d.split()
    if (len(sumit) != b) or (len(amit) != b):
        raise Exception
    sumit.sort()
    amit.sort()
    from copy import deepcopy
    sumit1 = deepcopy(sumit)
    amit1 = deepcopy(amit)
    i = 0
    ans1 = 0
    while (i < len(sumit)):
        j = 0
        while (j < len(amit)):
            if (sumit[i] < amit[j]):
                del sumit[i]
                del amit[j]
                j = b+1
            else:
                j = j+1
        if (j == len(amit)):
            ans1 = ans1 + len(sumit)
            i = b
    l = 0
    ans2 = 0
    while (l < len(amit1)):
        k = 0
        while (k < len(sumit1)):
            if (sumit1[k] < amit1[l]):
                del sumit1[k]
                del amit1[len(amit1)-1]
            else:
                del sumit1[k]
                del amit1[l]
                ans2 = ans2 + 1
    file2.write("Case #%s: %s %s\n" % (x,ans2,ans1))
    x = x+1
    a = a-1
file2.close()               
        
