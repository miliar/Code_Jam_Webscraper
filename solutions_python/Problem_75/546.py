infile="B-large.in"
outfile="data.out"
fin = open(infile, 'r')
fout = open(outfile, 'w')
buf = fin.readline()
T = int(buf)
for i in range(1, T+1):
    combine={}
    oppose=[]
    cur_list=['']
    buf = fin.readline()
    buf = buf.split()
    c = int(buf[0])
    buf = buf[1:]
    for k in range(c):
        key = buf[k][:-1]
        value = buf[k][-1]
        combine[key]=value
        key=key[::-1]
        combine[key]=value
        k+=1
    d = int(buf[c])
    buf = buf[c+1:]
    for k in range(d):
        value = buf[k]
        oppose.append(value)
        value = value[::-1]
        oppose.append(value)
        k+=1
    test_len = int(buf[d])
    buf = buf[d+1:]
    test = buf[0]
    ck = combine.keys()
    for k in range(len(test)):
        temp = test[k]+cur_list[-1]
        if temp in ck:
            cur_list=cur_list[:-1]
            cur_list.append(combine[temp])
        else:
            empty = False
            for j in range(len(cur_list)):
                if (cur_list[j]+test[k]) in oppose:
                    cur_list=['']
                    empty = True
                    break
            if empty == False:
                cur_list.append(test[k])
        k+=1
    buf = "Case #"+str(i)+": ["
    fout.write(buf)
    cur_list=cur_list[1:]
    outstr=''
    for s in range(len(cur_list)):
        outstr=outstr+cur_list[s]+', '
    outstr=outstr[:-2]
    fout.write(outstr)
    fout.write("]\n")
fin.close()
fout.close()
