#!/usr/bin/env python3
#
# Google code jam - qual round - 2014
# problem 1 - magic trick
#
# written by mark grandi - april 12 2014




import argparse, sys

def main(args):
    '''@param args - the arguments given to us by argparse.parse_args'''
    
    
    # here we parse the input
    
    # read the number of test cases
    numTestCases = int(args.inputFile.readline())
    
    for iterCaseNum in range(numTestCases):
    
        # read answer one
        answerOne = int(args.inputFile.readline())
        grid = []
        # read the grid
        for iterRow in range(4):
            # read the row, convert it to ints
            grid.append([int(x) for x in args.inputFile.readline().split(" ")] )
           

        # read answer two
        answerTwo = int(args.inputFile.readline())
        
        # read grid 2
        gridTwo = []
        for iterRow in range(4):
            # read the row, convert it to ints
            gridTwo.append([int(x) for x in args.inputFile.readline().split(" ")] )
        

        
        # now figure out the cards that were the row for the first answer
        answerOneRow = list()
        for count, iterRow in enumerate(grid, 1):
            if count == answerOne: # answers are one based
                answerOneRow = iterRow
                break
        
        
        # find the row of cards for the second answer
        answerTwoRow = list()
        for count, iterRow in enumerate(gridTwo, 1):
            if count == answerTwo: # answers are one based
                answerTwoRow = iterRow
                break
        
       
        # now find the cards that are common between the two rows
        
        answerSet = set(answerOneRow).intersection(set(answerTwoRow))
        
        
        prefixStr = "Case #{}: ".format(iterCaseNum + 1) # one based
        
        if (args.debug):
        
            args.outputFile.write("\trow: {}, chosenRowOne: {}\n".format( answerOne,answerOneRow))
            args.outputFile.write("\trow: {}, chosenRowTwo: {}\n".format(answerTwo, answerTwoRow))
            args.outputFile.write("\t\tintersection: {}\n".format(answerSet))
            
            
        if len(answerSet) == 0:
            args.outputFile.write("{}Volunteer cheated!\n".format(prefixStr))
        elif len(answerSet) == 1:
            args.outputFile.write("{}{}\n".format(prefixStr, list(answerSet)[0]))
        else:
            args.outputFile.write("{}Bad magician!\n".format(prefixStr))

if __name__ == "__main__":


    parser = argparse.ArgumentParser(epilog="Written by Mark Grandi - April 12 2014")


    parser.add_argument("inputFile", type=argparse.FileType("r"), help="the input file")
    parser.add_argument("outputFile", 
        nargs="?", type=argparse.FileType("w"), help="where to write the output, default is stdout")
    parser.add_argument("--debug", action="store_true", help="print debug messages")
    
    try:
        main(parser.parse_args())
    except Exception as e:
        print("An error occured: {}".format(e))
