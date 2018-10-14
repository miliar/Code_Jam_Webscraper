'''
Template

@author: Mohammad
'''
import math

def main():  
    inn = open("A-large.in", "r")
    out = open("out.txt", "w")
    T = int(inn.readline())
    for tt in range(T):
        [r, t] = [int(n) for n in inn.readline().split()]
        l = 0
        u = int(math.sqrt(t))
        out.write('Case #' + str(tt+1) + ': ')
        while l < u-1:
            m = (l + u)// 2
            if m * (2*m + 2*r - 1) > t:
                u = m-1
            else:
                l = m
        if  u * (2*u + 2*r - 1) > t:
            out.write(str(l))
        else:
            out.write(str(u))
        out.write('\n')
    inn.close()
    out.close()
main()
