'''
Created on 2012/04/14

@author: teraotsuyoshi
'''

def recycled(m, min):
    ms = str(m)
    ns = ms
    count = 0
    used = []
    for i in range(len(ms) - 1):
        ns = ns[1:] + ns[:1]
        n = int(ns)
        if m > n and n >= min and ( not n in used ):
            used.append(n)
            count = count + 1
    return count
    

def test(A, B):
    count = 0
    for m in range(A, B+1):
        count = count + recycled(m, A)
    return count

if __name__ == '__main__':
    lines = open("C-large.in").readlines()
    T = int(lines[0])
    for i in range(1, T+1):
        (A,B) = lines[i].split()
        A = int(A)
        B = int(B)
        print "Case #%d:"%(i), test(A,B)
         
        
                