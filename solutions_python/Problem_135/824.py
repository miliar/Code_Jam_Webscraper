#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      kiit
#
# Created:     10/04/2014
# Copyright:   (c) kiit 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from sets import Set
def list_int():
    m=raw_input()
    m=m.split()
    m= map(int,m)
    return m

def main():

    t=int (input())
    for i in range(t):
        d=[]
        c=[]
        m=[]
        n=int (input())
        d.append(list_int())
        d.append(list_int())
        d.append(list_int())
        d.append(list_int())
        qn=int(input())
        for x in range (4):
            c.append(list_int())


        m=[z for z in d[int(n - 1)] if (z in c[int(qn - 1)])]
        if (len(m) > 1):
            print 'Case #'+str(i+1)+': Bad magician!'
        elif(len(m)==0):
            print 'Case #'+str(i+1)+': Volunteer cheated!'
        else : print 'Case #'+str(i+1)+': '+ str(m[0])












if __name__ == '__main__':
    main()
