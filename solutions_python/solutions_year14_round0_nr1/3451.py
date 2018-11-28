# -*- coding: utf-8 -*-

in_file = open('/home/mariesnew/cj2014/A-small-attempt1.in','r')
n=int((in_file.readline()).strip())
ans = []
file_in_set = {}
for lineno,line in enumerate(in_file):
    file_in_set[lineno] = [int(i) for i in (line.strip()).split()]
    if lineno%5 == 0:
        ans.append(int(line.strip()))
j=0
file_list = []
for l in ans:
    file_list.append(file_in_set[j+l])
    j+=5
out_file = open('qr_a_2014.out','w')
line_index = 0
for k in range(0,len(file_list),2):
    sol_list = list(set(file_list[k]) & set(file_list[k+1]))
    if len(sol_list) == 1:
        out_file.write('Case #'+str(((k+1)/2)+1)+': '+str(sol_list[0])+'\n')       
    elif len(sol_list) == 0:
        out_file.write('Case #'+str(((k+1)/2)+1)+': '+'Volunteer cheated!'+'\n')      
    else:
        out_file.write('Case #'+str(((k+1)/2)+1)+': '+'Bad magician!'+'\n')
out_file.close()
in_file.close()

