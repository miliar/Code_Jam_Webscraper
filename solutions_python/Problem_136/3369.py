# -*- coding: utf-8 -*-

def cca(c,f,x):
    nc_per_sec = 2.0
    time_list = [(x/nc_per_sec)]
    if x <= c:
        return (x/nc_per_sec)
    else:
        first_cookie = c/nc_per_sec
        nc_per_sec+=f
        time_list.append(first_cookie+(x/nc_per_sec))
        i = 0
        while time_list[i+1] < time_list[i]:
            temp_time = first_cookie
            nc_per_sec = 2.0
            for j in range(1,i+3):
                if j != (i+2):
                    temp_time += c/(nc_per_sec+(f*j))
                else:
                    temp_time += x/(nc_per_sec+(f*j))
            time_list.append(temp_time)
            i+=1
        return time_list[i]
f_in = open('B-small-attempt0.in','r')
f_out = open('qr_b_2014.out','w')
input_dict = {}
n=int((f_in.readline()).strip())
for lineno, line in enumerate(f_in):
    input_dict[lineno]=[float(i) for i in ((line.strip()).split())]
for res in range(len(input_dict)):
    s = cca(input_dict[res][0],input_dict[res][1],input_dict[res][2])
    f_out.write('Case #'+str(res+1)+': '+str("%.7f"%s)+'\n')
f_in.close()
f_out.close()

