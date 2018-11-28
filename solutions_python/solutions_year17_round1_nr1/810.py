fin = open('C:\Users\zhaoyanjiao\Desktop\A-small-attempt2.in','r')
fout = open('C:\Users\zhaoyanjiao\Desktop\c.in.out','w')

count = 0
count_old = 0
printl = 0
case = 1
for line in fin:
    print line
    count += 1
    if count == 1:
        continue
    if count == 2:
        cols = line.strip().split()
        count_old = count
        R = int(cols[0])
        C = int(cols[1])
        
        list_t = []
        continue
    elif count - count_old > R:
        print list_t
        for k in range(len(list_t)):
            print k
            if list_t[k] != "?":
                elem = list_t[k]
                print "elem"
                print "shang"
                shang = k-C
                while shang>=0:
                    print shang
                    if list_t[shang] == "?":
                        list_t[shang] = elem
                    else:
                        break
                    shang = shang-C
                xia = k+C
                print "ssssss"
                while xia<len(list_t):
                    if list_t[xia]== "?":
                        list_t[xia] = elem
                    else:
                        break
                    xia = xia+C
                print "over"
            print "AAAAAA"
            print list_t
        flag = 0
        for i in range(C):
            if list_t[i] == "?":
                flag = 0
                xia = i + C
                while xia <len(list_t):
                    if list_t[xia] != "?":
                        flag = 1
                        break
                    xia = xia + C
                if flag == 0:
                    xia = i
                    for j in range(R):
                        if i >0:
                            print case
                            print R
                            print C
                            print xia
                            print list_t
                            list_t[xia] = list_t[xia-1]
                            xia = xia+C
                        else:   
                            list_t[xia] = list_t[xia+1]
                            xia = xia+C
        for i in range(C):
            i = C-i-1
            if list_t[i] == "?":
                flag = 0
                xia = i + C
                while xia <len(list_t):
                    if list_t[xia] != "?":
                        flag = 1
                        break
                    xia = xia + C
                if flag == 0:
                    xia = i
                    for j in range(R):
                        if i != C-1:
                            list_t[xia] = list_t[xia+1]
                            xia = xia+C
                        else:   
                            list_t[xia] = list_t[xia-1]
                            xia = xia+C
        fout.write("Case #" + str(case) + ":\n")
        for i in range(R):
            cont = ""
            print "100"
            print list_t
            for j in range(C):
                print j
                print i*C+j
                cont += list_t[i*C+j]
            fout.write(cont + "\n")
        cols = line.strip().split()
        count_old = count
        R = int(cols[0])
        C = int(cols[1])
        list_t = []
        case = case + 1
        continue
    else:
        cols = list(line.strip())
        list_t = list_t+cols
print "end"
        
fin.close()
fout.close()
