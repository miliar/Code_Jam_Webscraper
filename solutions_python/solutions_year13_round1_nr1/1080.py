'''
Created on Apr 26, 2013

@author: hou
'''
import sys
import math

def calculate_num(r, t):
    #Arithmetic progression
    a = 2*r - 1
    num = int((-a + math.sqrt(a*a + 8*t)) / 4)
    
    #revise num
    s = ((2*r + 1) + 2*(num-1))*num

    if s > t:
        return num - 1
    return num
    

def main():
    infile = open(sys.argv[1])          # input file as the first arg
    outfile = open(sys.argv[2], 'w')    # output file as the second arg

    # get the number of test cases
    test_num = int(infile.readline())
    
    for i in xrange(test_num):
        [r, t] = [int(elem) for elem in infile.readline().split()]
        circle_num = calculate_num(r, t)
        outfile.write("Case #" + str(i+1) + ": " + str(circle_num) + '\n')
        
    infile.close()
    outfile.close()


if __name__ == '__main__':
    main()