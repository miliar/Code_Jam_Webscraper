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

def is_it_possible(array):
    while True:
#        k=0
#        while(k < len(array)):
#            if array[k] is []:
#                del array[k]
#            k+=1
        if not array:
            break
        if not any(array):
            break
        
        minr=minc=0
        min=array[minr][minc]
        for r in range(len(array)):
            for c in range(len(array[0])):
                if array[r][c] < min:
                    minr = r
                    minc = c
                    min = array[r][c]
        numc = numr = 0
        rb = cb = True;
        
        
        for j in range(len(array[minr])):
            if array[minr][j] == min:
                numr+=1
        if numr != len(array[minr]):
            rb=False
                
        for j in range(len(array)):
            if array[j][minc] == min:
                numc+=1
        if numc != len(array):
            cb = False
            
        if not cb and not rb:
            return "NO"
                                        
        if cb:
           for j in range(len(array)):
               del array[j][minc]
        elif rb:
            del array[minr]
    return 'YES'

if __name__ == '__main__':
    actual_result = {}
    path = '/Users/ashishgaunkar/workspace/CodeJam/io/'+ 'lawnmover'
    ip_file = 'B-large.in'
    op_file = ip_file.split('.')[0]+'.op'
    lines = read_file(path, ip_file)
    total = int(lines[0])
    line=i=0
    ops = []
    while(i < total):
        i+=1
        line+=1
        N, M = [ int(n) for n in lines[line].split()]
        array = []
        for _ in range(N):
            line+=1
            array += [[ int(n) for n in lines[line].split()]]
        ops += [ "Case #{0}: {1}".format(i, is_it_possible(array))]
    write_file(path, op_file, ops)