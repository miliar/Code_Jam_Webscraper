filename = 'a.in'
r = open(filename,'r')
t = int(r.readline())
k = 1
w = open('out.txt','w')
ln = '\n'
while k<=t:
    b_pos = 1
    o_pos = 1
    line = r.readline().strip().split()
    num = int(line[0])
    pos = 1
    ttt = 0
    while pos < num * 2:
        obj = line[pos]
        dst = int(line[pos+1])
        if(obj=='O'):
            tt = abs(dst-o_pos)+1
            o_pos = dst
            temp = pos+2
            while temp < num*2:
                if (line[temp]=='B'):
                    break
                temp += 2
            if (temp < num *2):
                if(abs(int(line[temp+1])-b_pos) < tt):
                    b_pos = int(line[temp+1])
                else:
                    if(int(line[temp+1])>b_pos):
                        b_pos += tt
                    else:
                        b_pos -= tt
        if(obj=='B'):
            tt = abs(dst-b_pos)+1
            b_pos = dst
            temp = pos+2
            while temp < num*2:
                if (line[temp]=='O'):
                    break
                temp += 2
            if (temp < num *2):
                if(abs(int(line[temp+1])-o_pos) < tt):
                    o_pos = int(line[temp+1])
                else:
                    if(int(line[temp+1])>o_pos):
                        o_pos += tt
                    else:
                        o_pos -= tt

        ttt += tt    
        pos += 2
    w.write("Case #%d: %d" % (k,ttt) + ln)

    k += 1

r.close()
w.close()

