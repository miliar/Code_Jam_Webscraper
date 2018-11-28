#!/usr/bin/env python3
#
# Google code jam qualifier 2014
#
# B - Cookie Clicker Alpha 
#
# written by Mark Grandi - April 12 2014
#
#  


import argparse, sys, collections
import pprint

CookieResult = collections.namedtuple("CookieResult", ["numOfFarms", "totalTime"])

def main(args):
    '''@param args - the arguments given to us by argparse.parse_args'''
    
    
    # read in number of test cases
    numTestCases = int(args.inputFile.readline())
    
    for iterCaseNum in range(numTestCases): # case numbers start at 1 as a FYI
    
    
        # read in the values
        tmpLine = args.inputFile.readline()
        cookieFarmCost, extraCookiesFromFarm, cookieGoal = [float(tmp) for tmp in tmpLine.split(" ")]
        
        originalCookiesPerSecond = 2
        
        if args.debug:
            args.outputFile.write("###########################\n")
            args.outputFile.write("\tCookie farm cost: {}, extra cookies from farm: {}, cookieGoal: {}\n"
                .format(cookieFarmCost, extraCookiesFromFarm, cookieGoal))
        
        
        numFarmsCounter = 0
        lowestTime = None
        while True:
            
            
            iterCookiesPerSec = originalCookiesPerSecond
            runningTimeTotal = 0
            
            # for x number of farms that we are going to test
            for tmpFarmCounter in range(numFarmsCounter):
            
                # add the time to buy one farm
                runningTimeTotal += cookieFarmCost / iterCookiesPerSec
                iterCookiesPerSec += extraCookiesFromFarm
                
                # now at 0 cookies again
                
            # now done with purchasing farms, add the time to just go from where we are 
            # at (0 cookies) to get to cookieGoal
            
            runningTimeTotal += cookieGoal / iterCookiesPerSec
            
            # check result
            if lowestTime == None:
                lowestTime = runningTimeTotal
                
            elif runningTimeTotal < lowestTime:
                lowestTime = runningTimeTotal
            else:
                break
            numFarmsCounter += 1
            
        if args.debug:
            args.outputFile.write(pprint.pformat(results, indent=8) + "\n")
            
                    
                    
            
        prefixStr = "Case #{}: ".format(iterCaseNum + 1) # one based
        args.outputFile.write("{}{:.7f}\n".format(prefixStr, lowestTime))
            

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="Problem B - Cookie clicker alpha - google code jam qual 2014",
        epilog="Written by Mark Grandi - April 12 2014")


    parser.add_argument("inputFile", type=argparse.FileType("r"), help="the input file")
    parser.add_argument("outputFile", 
        nargs="?", type=argparse.FileType("w"), default=sys.stdout,
        help="where to write the output, default is stdout")
    parser.add_argument("--debug", action="store_true",  help="print debug messages")
    parser.add_argument("--numFarmPrecision", type=int, default=100, 
        help="The number of iterations (of buying 0-X) number of farms), larger numbers = more accurate")
    
    try:
        main(parser.parse_args())
    except Exception as e:
        print("An error occured: {}".format(e))
        
        
        
        
