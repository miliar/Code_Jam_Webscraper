import math

__author__ = 'uritwig'

def main():

    #fp = open('example.txt','r')
    fp = open('C-small-attempt0.in','r')


    cases =  int(fp.readline())

    for case in range(0,cases):

        V = [int(i) for i in fp.readline().split(' ')]

        num = 0
        for i in range(V[0],V[1]):
            for j in range(0,len(str(i))):
                perm =  int(str(i)[j:] + str(i)[0:j])

                if i < perm and len(str(i)) == len(str(perm)) and perm >= V[0] and perm <= V[1]:
                    num += 1

        print 'Case #%d: %d' % (case+1,num)
        

                






main()