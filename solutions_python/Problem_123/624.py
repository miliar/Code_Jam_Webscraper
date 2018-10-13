'''
Created on May 4, 2013

@author: ashishgaunkar
'''
def read_file(path, filename):
    lines = [line.strip() for line in open(path+ '/' +filename) if line != '\n']
    return lines

def write_file(path, filename, ops):
    with open (path+ '/' +filename, 'w') as f:
        for o in ops:
            f.write (o+'\n')

def is_add_possible(master, m, i, num, v):
    k=0
    orig_master = master
    master = 2*master-1
    limit = (num-(i+1))
    while(master <= m and k < limit):
        master = 2*master-1
        k+=1
    if k >= limit:
        k = 0
        master = orig_master
    return k, master
        

def calculate(master, num, motes):
    '''
    check # of operations
    assume : motes are sorted
    '''       
    v = 0
    for i, m in enumerate(motes):
        if master > m:
            master += m
            continue
        else:
            v +=1
            if (2*master -1)>m:
                master=2*master-1+m
            else:
                k, master = is_add_possible(master, m, i, num, v)
                if k:
                    master +=m
                v +=k
                    
    return v
        
if __name__ == '__main__':
    actual_result = {}
    path = '/Users/ashishgaunkar/workspace/CodeJam/io/'+ 'osmos'
    ip_file = 'A-small-attempt3.in'
    #ip_file = 'test.in'
    op_file = ip_file.split('.')[0]+'.op'
    lines = read_file(path, ip_file)
    total = 2*int(lines[0])
    i=0
    ops=[]
    i+=1
    k=0
    while(i < total):
        master, num = [int(n) for n in lines[i].split(' ')]
        motes = [int(n) for n in lines[i+1].split(' ')]
        #print master, num, motes
        value = calculate(master, num, sorted(motes))
        k+=1
        ops += [ "Case #{0}: {1}".format(k, value)]
        
        i +=2
    write_file(path, op_file, ops)