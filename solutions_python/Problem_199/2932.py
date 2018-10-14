import sys
import os
import re


#define a function to verify test string
def pancakeFlipper(str):
    lineString = re.split('\s+', str)
    pancakeString = lineString[0]
    numberCanFlip = int(lineString[1])
    # print(pancakeString, numberCanFlip)
    up = "+"
    down = "-"
    getFlipNum(str = pancakeString, int = numberCanFlip)
    return
    
def getFlipNum(str, int):  
    flipNum = 0;    
    while True:
        
        # find first down
        i = str.find("-")
        # if there is no down
        if i == -1:
            print(flipNum)
            return
            
        # if number of pancake can flip is smaller than the tool size
        elif len(str) - i < int:
            print("IMPOSSIBLE")
            return
            
        # flip
        else:
            flipNum += 1
            string = list(str)
            for j in range(0, int):
                if string[i + j] == "+":
                    string[i + j] = "-"
                else:
                    string[i + j] = "+"
            str = ''.join(string) 
            
def main():
    # open and read input file
    content = []
    with open("input.txt") as f:
        content = f.read().splitlines()

        # get first line number as number of iterations
        iterateNum = int(content[0])

    # get each line of test string
    i = 1
    for lineString in range(1, iterateNum + 1):
        print("Case #" + str(i) + ": ", end = "")
        i += 1
        pancakeFlipper(str = content[lineString])
        
    

        f.close()
  
  
# calling main function  
main()