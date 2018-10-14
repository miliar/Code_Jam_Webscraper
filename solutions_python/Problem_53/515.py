'''
Created on May 7, 2010

@author: Isabelle
'''
import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    # process arguments
    filename = 'A-large'
    input = open(filename+'.in')
    output = open(filename+'.out', 'w')

    T = int(input.readline().strip())
    
    for i in range(0,T):
        (N,K) = [int(x) for x in input.readline().strip().split()]
        output.write('Case #' + str(i+1) + ': ')
        if (K+1) % pow(2,N) == 0:
            output.write('ON\n')
        else:
            output.write('OFF\n') 
    input.close()
    output.close()
    
    
if __name__ == "__main__":
    main()
