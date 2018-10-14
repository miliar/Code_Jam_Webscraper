import sys

x = 0;
n = sys.stdin.readline()
n = int(n)


while (x < n):
    x = x + 1 #count
    
    rt = sys.stdin.readline().split()
    
    w = rt[0]
    l = int(rt[1])
    
    list = []
    
    for i in range(len(w) + 1):
        if (i >= l):
            for j in range(len(w)):
                if j + i <= len(w):
                    list.append(w[j: j + i])
    
    count = 0
    for i in list:
        iter = 0
        for j in range(len(i)):
            if (i[j] != 'a' and i[j] != 'e' and i[j] != 'i' and i[j] != 'o' and i[j] != 'u'):
                iter = iter + 1
            elif iter < l:
                iter = 0
        if (iter >= l):
            count = count + 1
    print("Case #",x,": ",count, sep='')