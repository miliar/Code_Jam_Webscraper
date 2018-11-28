'''
Created on 07/05/2011

@author: German
'''

def it_recycled(n):
    s = str(n)
    s1 = s
    while 1:
        d = s1[-1]
        s1 = d + s1[:-1]
        if d !='0':
            yield int(s1)
        if s1 == s:
            return

def recycled(A, B):
    r = 0
    for n in range(A, B+1):
        for m in it_recycled(n):
            if n < m and m <= B:
                r +=1
    return r 

if __name__ == '__main__':
    with open('sol.out', 'w') as out:
        with open('C-large.in', 'r') as f:
            T = int(f.readline())
            for i in xrange(1,T+1):
                [A, B] = [int(x) for x in f.readline().split()]
                
                res = recycled(A,B)
                                
                res_str = "Case #%d: %d\n" % (i, res)
                print res_str,
                out.write(res_str)