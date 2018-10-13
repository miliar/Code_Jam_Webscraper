def score(l, i):
    count = 0
    flag = 0
    s = int(l[1])
    p = int(l[2])
    l1 = l[3:]
    l1 = map(int, l1)
    l1.sort()
    t = 0
    for j in l1:
        temp = int(j) - p
        temp /= 2
        if flag == 1 and j>= t:
            count += 1
        elif temp >= p-1 and temp >= 0:
            count += 1
            flag = 1
            t = j
        elif temp >= p-2 and temp >= 0 and s>=1:
            count += 1
            s -= 1
    file2 = open("dance_out.txt",'a')
    file2.write("Case #"+str(i)+": "+str(count))
    file2.write("\n")
    file2.close()
    

file1 = open("dance_in.txt", 'r')
n = int(file1.readline())
for i in range(n):
    l = file1.readline()
    s = l.split()
    score(s, i+1)

