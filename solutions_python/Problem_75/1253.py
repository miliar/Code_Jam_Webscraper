# To change this template, choose Tools | Templates
# and open the template in the editor.


from os.path import abspath


__author__="posv"
__date__ ="$May 7, 2011 3:37:55 PM$"

fin = open(abspath("/Users/posv/NetBeansProjects/Magicka/input.txt"))
fout = open(abspath("/Users/posv/NetBeansProjects/Magicka/output.txt"),"w")
x1 = []
i = 1
t = int(fin.readline())
while True:
    str1 = fin.readline()
    if not str1:
	break
	#print str
    lst = str1.split()
    if(len(lst) == 4):
        x1 = list(lst[3])
    if(len(lst) == 5):
        if int(lst[0]) == 0:
            #cn = int(lst[0])
            #cs = list(lst[1])
            dn = int(lst[1])
            ds = list(lst[2])
            n = int(lst[3])
            s = list(lst[4])
            s.reverse()
            temp = cs[0:2]
            temp.reverse()
            x1 = s[0:0]
            x1.append(s.pop())
            while s:
                x1.append(s.pop())
                dni = 0;
                while(dni < dn*2):
                    if ds[dni] in x1 and ds[dni+1] in x1:
                        x1 = []
                        if(len(s) == 0):
                            break
                        x1.append(s.pop())
                    dni = dni+2
        elif int(lst[2]) == 0:
            cn = int(lst[0])
            cs = list(lst[1])
            #dn = int(lst[1])
            #ds = list(lst[2])
            n = int(lst[3])
            s = list(lst[4])
            s.reverse()
            temp = cs[0:2]
            temp.reverse()
            x1 = s[0:0]
            x1.append(s.pop())
            while s:
                x1.append(s.pop())
                cni = 0
                while(cni < cn*3):
                    if cs[cni:cni+2] == x1[len(x1)-2:] or temp == x1[len(x1)-2:]:
                        x1[len(x1)-2:] = cs[cni+2]
                    cni = cni + 3
    if(len(lst) == 6):
        cn = int(lst[0])
        cs = list(lst[1])
        dn = int(lst[2])
        ds = list(lst[3])
        n = int(lst[4])
        s = list(lst[5])
        s.reverse()
        temp = cs[0:2]
        temp.reverse()
        #print x1
        x1 = s[0:0]
        x1.append(s.pop())
        while s:
            x1.append(s.pop())
            cni = 0
            while(cni < cn*3):
                if cs[cni:cni+2] == x1[len(x1)-2:] or temp == x1[len(x1)-2:]:
                    x1[len(x1)-2:] = cs[cni+2]
                cni = cni + 3
            dni = 0;
            while(dni < dn*2):
                if ds[dni] in x1 and ds[dni+1] in x1:
                    x1 = []
                    if(len(s) == 0):
                        break
                    x1.append(s.pop())
                dni = dni+2
    case1 = 'Case #'+str(i)+': '
    case2 = "["
    if len(x1) == 0:
        case2 = case2 + "]"
    else:
        for chr in range(0,len(x1)):
            if(chr == (len(x1)-1)):
                case2 = case2 +x1[chr]+"]"
            else:
                case2 = case2 +x1[chr]+", "
    fout.write(case1 + case2)
    #fout.writelines(x1)
    fout.write('\n')
    i = i + 1