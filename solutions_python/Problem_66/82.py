'''
Created on 2010/06/05

@author: banana
'''

if __name__ == '__main__':
    pass


fp = open("B-small-attempt1.in", "r")

line = fp.readline()

T = int(line)

fpout = open("B-small.txt", "w")

for t in xrange(1, T+1):
    line = fp.readline()
    P = int(line)
    M = fp.readline().split()
    M = [int(x) for x in M]
    
    count = pow(2, P)
    
    price = list()
    for i in range(P):
        price.append([int(x) for x in fp.readline().split()])
        
    price2 = list()
    for i in range(P):
        for k in price[i]:
            price2.append(k)

    
    ranges = list()
    step = count
    a = 0
    for i in range(count-1):
        ranges.append((a, a + step-1))
        a = a + step
        if a == count:
           step = step / 2
           a = 0 
    
    need = list()
    for i in range(count):
        need.append(P - M[i])    
    
    cost = 0
    
    for (a,b) in ranges:
        if max(need[a:b+1]) > 0:
            cost = cost + 1
            for i in range(a,b+1):
                need[i] = need[i] - 1
        
    
    fpout.write("Case #%d: %d\n"%(t, cost))
    print "Case #%d: %d"%(t, cost)