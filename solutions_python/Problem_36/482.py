import sys
import os
import string

def main():
	s = sys.stdin.readlines()
	os.close(0)
        s = map(lambda X: X[:-1], s)
    #    print s
        
        N = int(s[0])
        s = s[1:]
        cases = map(lambda X: ''.join([item for item in X if item in 'welcome to code jam']), s)
        cases = map(lambda X: X[X.find('w'):X.rfind('m')+1], cases)
        #cases = s
    #    print cases

        for i in range(N):
            print "Case #" + str(i+1) + ": " + (string.zfill(str(codejams(cases[i])), 4))[-4:]

def codejams(case):
    phrase = 'welcome to code jam'
    if len(case) < len(phrase):
        return 0
    dpmat = []
    for j in range(len(case)):
        dpmat += [[]]
        for k in range(len(phrase)):
            if j==k==0:
                dpmat[j] += [1]
            elif j < k:
                dpmat[j] += [0]
            else:
                dpmat[j] += [[]]
    for i in range(1, len(case)):
        for j in range(len(phrase)):
            if case[i] == phrase[j] and not j == 0:
                dpmat[i][j] = dpmat[i-1][j] + dpmat[i-1][j-1]
            elif case[i] == phrase[j] and j==0:
                dpmat[i][j] = dpmat[i-1][j] + 1
            else:
                dpmat[i][j] = dpmat[i-1][j]
    #printMat(dpmat)
    return dpmat[len(case)-1][len(phrase)-1]

def printMat(dpmat):
    for i in range(len(dpmat)):
        printStr = ""
        for j in range(len(dpmat[0])):
            printStr += str(dpmat[i][j]) + " "
        print printStr
            
    
if __name__ == "__main__":
 	main()

