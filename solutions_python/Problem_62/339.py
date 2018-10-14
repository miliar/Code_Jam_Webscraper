#!/usr/bin/env python

SET_NAME = 'A-small'



def solve_case(infile):
    count=0
    mat=[]
    n=int(infile.readline())
    print n
    for i in xrange(n):
        mat.append(map(int, infile.readline().split()))
    print mat
    for i in range(n-1):
        for j in range(i+1,n):
            print mat[i],mat[j]
            count=count+control(mat[i],mat[j])
    return count

def control(list1,list2):
    print list1,list2

    print type(list1[1])
    if (list1[0]>list2[0] and list1[1]>list2[1]) or (list1[0]<list2[0] and list1[1]<list2[1]):
        return 0
    else:
        print 1
        return 1


def main():
    """
    Standard main method for all google code jam problems
    """
    infile = open('%s.in'%(SET_NAME))
    outfile = open('%s.out'%(SET_NAME), 'w')
    num_cases = int(infile.readline())
    for i in xrange(num_cases):
        print 'Solving case #%d...'%(i+1)
        output = 'Case #%d: %s\n'%(i+1, solve_case(infile))
        print output
        outfile.write(output)
    outfile.close()
if __name__ == '__main__':
    main()
