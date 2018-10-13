def recycle_nos(l, k):
    count = 0
    low = int(l[0])
    high = int(l[1])
    no_list = range(low, high + 1)
    for i in no_list:
        temp = [] 
        string = list(str(i))
        length = len(string)
        if i > 10:
            m = i
            for j in range(0, length - 1):
                p = string.pop(-1)
                string.insert(0, p)
                if p != '0':
                    n = int("".join(string))
                    if(n >= low and n <= high and n!= m and n > i):
                        if n not in temp:
                            count += 1
                            temp.append(n)
                        
    fout = open("output.txt", 'a')
    fout.write("Case #" + str(k) + ": ")
    fout.write(str(count))
    fout.write("\n")
    fout.close()                    
                
fin = open("file.txt", 'r')
n = int(fin.readline())

for i in range(n):
    line = fin.readline()
    split_line = line.split()
    recycle_nos(split_line, i+1)
    
