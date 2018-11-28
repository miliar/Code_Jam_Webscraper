#google code jam 2010 Round 1B
#Javier Fernandez javierfdr@gmail.com

import sys

#length
def dir_len(dir):
    return dir.count('/')

def add_all(dir_list,ddir):
    ldir = ddir.split('/')[1:]
    for n in range(1,dir_len(ddir)+1):        
        s = take_n(ldir,n)
        add_dir(dir_list,s,n)

def add_dir(dir_list,ddir,dlen):
    #dlen = len(dir_list)
    dir_l = len(dir_list)
    if(dlen<=dir_l):
        if ddir in dir_list[dlen-1]:
            return False
    elif(dlen>dir_l):
        for i in range(dir_l,dlen):            
            dir_list.append({})
    dir_list[dlen-1][ddir] = True

def take_n(list_dir, n):
    return '/'+'/'.join([list_dir[x] for x in range(n)])
    
def count_mkdir(o_list,new_dir):
    num_dir = dir_len(new_dir)
    s_dir = new_dir.split('/')[1:]
    n = len(o_list)
    if(num_dir>n):
        sum_mkdir = num_dir-n
    else:
        n = num_dir
        sum_mkdir = 0
    while(n>0):
        part = take_n(s_dir,n)
        if part in o_list[n-1]:
            return sum_mkdir
        sum_mkdir+=1
        n-=1
    return num_dir

out_file = open('output.out','w+')
in_file = sys.stdin
num_cases = int(in_file.readline())
#in_file.readline()
#num_cases = 1

for c in range(1,num_cases+1):
    O,S = map(int,in_file.readline().strip('\n').split())

    original_list=[{'/':True}]
    for o in range(O):
        new_dir = in_file.readline().strip('\n')
        add_all(original_list,new_dir)

    search_list=[]
    for s in range(S):
        new_dir = in_file.readline().strip('\n')
        search_list.append(new_dir)

    c_mkdir = 0
    for new_dir in search_list:
        new_count = count_mkdir(original_list,new_dir)        
        if(not new_count==0):
            add_all(original_list,new_dir)
            c_mkdir+= new_count
        
    case = 'Case #'+str(c)+': '
    out_file.write(case+str(c_mkdir)+'\n')
        
