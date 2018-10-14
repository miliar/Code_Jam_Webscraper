fin = open('G:\A-large.in','r')
fout = open('G:\A-large.out','w')

count = -1
printl = 0
for line in fin:
    cishu = 0
    count = count + 1
    cols = line.strip().split()
    if count == 0:
        continue
    stall_num = int(cols[0])
    p_num = int(cols[1])
    stall_list = []
    stall_list.append(stall_num)
    for i in range(p_num):
        max_len = 0
        max_label = 0
        for k in range(len(stall_list)):
            if stall_list[k] > max_len:
                max_len = stall_list[k]
                max_label = k
        del stall_list[max_label]
        if max_len != 1:
            if max_label == 0:
                list_left = []
            else:
                list_left = stall_list[0:max_label]
            list_right = stall_list[max_label:]
            if max_len % 2 == 1: 
                list_left.append(max_len/2)
                list_left.append(max_len/2)
                stall_list = []
                stall_list = list_left+list_right
                if i == p_num - 1:
                    fout.write("Case #%d: %d %d\n" %(count, max_len/2, max_len/2))
            else:
                if max_len == 2:
                    list_left.append(max_len/2)
                    stall_list = []
                    stall_list = list_left+list_right
                    if i == p_num - 1:
                        fout.write("Case #%d: %d %d\n" %(count, max_len/2, 0))
                else:
                    list_left.append(max_len/2-1)
                    list_left.append(max_len/2)
                    stall_list = []
                    stall_list = list_left + list_right
                    if i == p_num - 1:
                        fout.write("Case #%d: %d %d\n" %(count, max_len/2, max_len/2-1))
            
        else:
            if i == p_num - 1:
                fout.write("Case #%d: %d %d\n" %(count, 0, 0))
    
fin.close()
fout.close()