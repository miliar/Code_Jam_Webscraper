'''
Created on 14 Apr 2012

@author: rich
'''


def recyclednumbers(fin,fout):
    f = open(fin,'r')
    fout = open(fout,'w')
    
    is_first = True
    t = 1
    for r in f:
        if is_first:
            T = r
            is_first = False
        else:
            arr = r.split(' ')
            A = int(arr[0])
            B = int(arr[1])
            print A,B
            n = get_recycled_pairs(A,B)
            fout.write('Case #' + str(t) + ': ' + str(n) + '\n')
            t += 1
    
def get_recycled_pairs(A,B):
    ints = {}
    for i in range(A,B+1):
        s = get_sorted_int(i)
        if ints.has_key(s):
            ints[s].append(i)
        else:
            ints[s] = [i]
    
    print ints
    cyclic_pairs = []
    for s in ints.keys():
        a = ints[s]
        l = len(s)
        al = len(a)
        if al>1:
            for j in range(0,al-1):
                for k in range(j+1,al):
                    if is_cyclic_pair(a[j],a[k],l):
                        cyclic_pairs.append([a[j],a[k]])
        
    print cyclic_pairs
    print len(cyclic_pairs)
    return len(cyclic_pairs)
            
    
def get_sorted_int(i):
    s = str(i)
    a = []
    for j in range(0,len(s)):
        a.append(s[j:j+1])
    a.sort()
    return ''.join(a)

def is_cyclic_pair(i,j,l):
    
    a = str(i)
    b = str(j)    

    # find all the matches in b for the first char of a
    matches = {}
    for i in range(l):
        m = b.find(a[0],i)
        if m > -1 and not matches.has_key(m):
            matches[m] = ''
    
    for offset in matches.keys():
        is_cyclic = True
        for k in range(1,len(a)):
            if b[(offset + k)%l] <> a[k]:
                is_cyclic = False
                break
        if is_cyclic == True:
            break
        
    return is_cyclic


if __name__ == '__main__':
    pass

fin = 'C:\\Users\\rich\\Documents\\codejam\\C-small-attempt0.in'
fout = 'C:\\Users\\rich\\Documents\\codejam\\C-small-attempt0.out'
recyclednumbers(fin,fout)

#print is_cyclic_pair(203,302,3)
#s = get_sorted_int(12345)
#print s,len(s)
