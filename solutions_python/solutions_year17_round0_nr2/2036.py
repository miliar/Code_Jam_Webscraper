#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      makkron
#
# Created:     08/04/2017
# Copyright:   (c) makkron 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys,math

def idNumber(num,idx):
    return (num // (10 ** (idx)) % 10)

def lenNum(num):
    #input strictly positive
    return len(str(num))

def main():
    nbSample=int(input())
    for idSample in range(nbSample):
        tatianaNumber = int(sys.stdin.readline())
        sentry=lenNum(tatianaNumber)-1
        for idNum in range(lenNum(tatianaNumber)-1,-1,-1):
            if idNum == 0:
                print("Case #{}: {}".format(idSample+1,tatianaNumber))
                break
            elif idNumber(tatianaNumber,idNum) > idNumber(tatianaNumber,idNum-1):
                decal = 10 ** (sentry)
                print("Case #{}: {}".format(idSample+1,(tatianaNumber // decal) * decal -1))
                break
            elif idNumber(tatianaNumber,idNum) < idNumber(tatianaNumber,idNum-1):
                sentry=idNum-1

if __name__ == '__main__':
    main()