'''
Created on May 7, 2010

@author: Isabelle
'''
import sys

def main(argv=None):
    if argv is None:
        argv = sys.argv
    # process arguments
    filename = 'C-small-attempt1'
    input = open(filename+'.in')
    output = open(filename+'.out', 'w')

    T = int(input.readline().strip())
    
    for i in range(0,T):
        (R,k,G) = [int(x) for x in input.readline().strip().split()]
        groups = [int(x) for x in input.readline().strip().split()]
        profit = 0
        for j in range(0,R):
            numRiders = 0
            new_groups = []
            while len(groups) > 0 and numRiders + groups[0] <= k:
                numRiders += groups[0]
                g = groups.pop(0)
                new_groups.append(g)
            profit += numRiders
            groups += new_groups
        output.write('Case #' + str(i+1) + ': ' + str(profit) + '\n')
    input.close()
    output.close()
    
    
if __name__ == "__main__":
    main()
    