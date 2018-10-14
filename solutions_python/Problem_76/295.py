'''
Created on 2010/05/08

@author: banana
'''

if __name__ == '__main__':
    pass

fp = open("C-large.in", "r")

lines = fp.readlines()

T = int(lines[0])

fpout = open("C-large.txt", "w")

for t in range(1, T+1):
    l = [ int(x) for x in lines[t*2].split()]

    #check if divisible
    M = 22
    bitcount = [ 0 for x in range(M) ]
    div = 1
    nondiv = False
    for i in range(M):
        rem = 0
        for x in l:
            rem = rem + ((x / div) % (div * 2))
        bitcount[i] = rem
        div = div * 2
        if rem % 2 == 1:
            nondiv = True
            break
    
    if nondiv:   
        fpout.write("Case #%d: NO\n"%(t))      
    else:
        l.sort()
        s = sum(l[1:])
        fpout.write("Case #%d: %d\n"%(t, s))   
         
fpout.close()