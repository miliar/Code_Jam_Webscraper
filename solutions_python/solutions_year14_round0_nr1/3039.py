#!/usr/bin/python
import sys,os


def solve(index1, grid1, index2, grid2):
    """Returns a string result to one case of a problem"""
    intersection = set(grid1[index1]) & set(grid2[index2])
    if len(intersection) > 1 :
        return "Bad magician!"
    if len(intersection) < 1 :
        return "Volunteer cheated!"
    return intersection.pop()

#Shared########################################################################
def main():
    with open(sys.argv[1], 'rU') as f_in:
        cases = int(f_in.readline().strip())
        for case in range(1,cases+1):

            #Get input data
            index1 = int(f_in.readline().strip()) - 1
            grid1 = [[int(x) for x in f_in.readline().strip().split()] for _ in range(4)]
            index2 = int(f_in.readline().strip()) - 1
            grid2 = [[int(x) for x in f_in.readline().strip().split()] for _ in range(4)]
            #Solve and output
            print("Case #{}: {}".format(case, solve(index1, grid1, index2, grid2)))
    
if __name__ == '__main__':
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        main()
    elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1]):
        print "File '"+str(sys.argv[1])+"' does not exist!"
    else:
        print "No file supplied! Run program this way: '"+str(sys.argv[0])+" something.in'"
        
