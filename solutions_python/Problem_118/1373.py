'''
Created on Apr 13, 2013

@author: ashishgaunkar
'''
'''
Created on Apr 13, 2013

@author: ashishgaunkar
'''
def read_file(path, filename):
    lines = [line.strip() for line in open(path+ '/' +filename) if line != '\n']
    return lines

def write_file(path, filename, ops):
    with open (path+ '/' +filename, 'a') as f:
        for o in ops:
            f.write (o+'\n')
            
import math
def is_square(number):
    temp = math.sqrt(int(number))   
    #print str(abs(temp)).split('.')[1] == '0'
    if str(abs(temp)).split('.')[1] is '0':
        return True
    else:
        return False
    
def is_fare_n_square(number):
    v = False
    if is_square(number):
        n = str(number)
        root = str(int(math.sqrt(number)))
        v =  n == n[::-1] and root == root[::-1]
    return v

             
if __name__ == '__main__':
    actual_result = {}
    path = '/Users/ashishgaunkar/workspace/CodeJam/io/'+ 'fair-square'
    ip_file = 'C-small-attempt0.in'
    op_file = ip_file.split('.')[0]+'.op'
    lines = read_file(path, ip_file)
    total = int(lines[0])
    line=case=0
    ops=[]
    while(case < total):
        case+=1
        line+=1
        st, en =[int(n) for n in lines[line].split(" ")]
#        print st , en
        total_far_sq = len ([n for n in range(st, en+1) if is_fare_n_square(n)])
        ops += ["Case #{0}: {1}".format(case, str(total_far_sq))]
    write_file(path, op_file, ops)