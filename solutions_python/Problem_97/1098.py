def recycle(l, x):
    count = 0
    flag = 0
    r1 = int(l[0])
    r2 = int(l[1])
    lst = range(r1, r2+1)
    for i in lst:
        temp = [] 
        s = list(str(i))
        ln = len(s)
        if i > 10:
            m = i
            for j in range(0,ln-1):
                p = s.pop(-1)
                s.insert(0,p)
                if p != '0':
                    n = int("".join(s))
                    if(n >= r1 and n <= r2 and n!= m and n > i):
                        if n not in temp:
                            count += 1
                            temp.append(n)
                        
    file2 = open("output.txt", 'a')
    file2.write("Case #"+str(x)+": ")
    file2.write(str(count))
    file2.write("\n")
    file2.close()                    
                
file1 = open("C-small-attempt0.in", 'r')
n = int(file1.readline())
for i in range(n):
    l = file1.readline()
    s = l.split()
    recycle(s, i+1)
    
