import sys
import re
import math

def getOvation(sMax, s):
        count =0
        sol=0

        for i in range(len(s)):
                if (i > count):
                        sol += (i-count)
                        count = i
                count += int(s[i])
        return sol
                

       
def main(file):
        f = open(file, 'r')
        T = int(f.readline())

        fo = open('A-large.out', 'w')
        stage = 0
        while stage < T:
                S = f.readline().split()
                k = getOvation(int(S[0]),S[1])
                stage += 1
                fo.write("Case #" + str(stage) + ": " + str(k) + "\n")

if __name__ == '__main__':
        main('A-large.in')
        
