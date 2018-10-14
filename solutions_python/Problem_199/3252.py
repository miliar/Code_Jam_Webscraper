fin = open('C:\Users\zhaoyanjiao\Desktop\A-small-attempt4.in','r')
fout = open('C:\Users\zhaoyanjiao\Desktop\A-small-practice.out2','w')

count = -1
printl = 0
for line in fin:
    cishu = 0
    count = count + 1
    cols = line.strip().split()
    if count == 0:
        continue
    str1 = cols[0]
    num = int(cols[1])
    str_list = list(str1)
    total = 1
    for elem in str_list:
        if elem == "-":
            total = 0
    if total == 1:
        if printl != 0:
            fout.write("\n")
        printl += 1
        fout.write("Case #%d: %d" %(count, cishu))
            
        continue
    for i in range(len(str_list)):
        if str_list[i] == "-":
            qi = i
            wei = i+num
            if wei > len(str_list):
                wei = len(str_list)
                total = -1
                break
            for j in range(qi,wei):
                if str_list[j] == "-":
                    str_list[j] = "+"
                else:
                    str_list[j] = "-"
            cishu += 1
        total = 1
        for elem in str_list:
            if elem == "-":
                total = 0
        if total == 1:
            break
    if total == 1:
        if printl != 0:
            fout.write("\n")
        printl += 1
        fout.write("Case #%d: %d" %(count, cishu))
        continue
    elif total == -1:
        if printl != 0:
            fout.write("\n")
        printl += 1
        fout.write("Case #%d: %s" %(count, 'IMPOSSIBLE'))
    
fin.close()
fout.close()