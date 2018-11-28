'''
Created on Apr 11, 2014

@author: mandy
'''
import sys

def cookieClicker(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    numTests = int(lines[0])
    
    for i in xrange(numTests):
        currentTest = lines[i+1].strip('\n').split(' ')
        numCookies = 0
        cookiesRate = 2
        numFarms = 0
        time = 0
        C = float(currentTest[0])
        F = float(currentTest[1])
        X = float(currentTest[2])
        while timeForUsingCurrentSource(numFarms, numCookies, cookiesRate, C, F, X) > timeForGettingOneMoreFarm(numFarms, numCookies, cookiesRate, C, F, X):
            time += C/cookiesRate
            numFarms += 1
            cookiesRate += F
            numCookies = 0
        print 'Case #'+str(i+1)+': '+str(time+X/cookiesRate)

def timeForUsingCurrentSource(numFarms, numCookies, cookiesRate, C, F, X):
    t = X/cookiesRate
    return t
    
def timeForGettingOneMoreFarm(numFarms, numCookies, cookiesRate, C, F, X):
    t = C/cookiesRate+X/(cookiesRate+F)
    return t

def main():
    currentPath = sys.argv[0]
    currentPath = currentPath[:currentPath.rfind('/')]
    file = currentPath+'/B-large.in'
    cookieClicker(file)

if __name__ == '__main__':
    main()